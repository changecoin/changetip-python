# coding=utf-8
import settings
import logging
import json
import re
import requests

logger = logging.getLogger(__name__)


class BaseBot(object):

    # Override this with the name of the channel.Must have correspond
    # The API must know about it ahead of time
    # To register a new bot, contact info@changetip.com
    changetip_api_key = None  # api key for the bot to submit transactions
    username = None  # username on the site
    prefix = "@"
    last_context_uid = None
    proxy = None
    # How many seconds the bot runner should wait before checking for new tips
    new_tip_check_delay = 15

    def __str__(self):
        return "%s bot with %s proxy %s" % (self.__class__.__name__, self.username, self.proxy)

    @property
    def name(self):
        return self.__class__.__name__.lower()

    def mention_bot(self):
        return "%s%s" % (self.prefix, self.username)

    def mention(self, username):
        return '%s%s' % (self.prefix, username)

    def check_for_new_tips(self, last):
        """ Poll the site for new tips. Expected to return an array of tips, in the format passed to handle_tip """
        raise NotImplementedError

    def handle_tip(self, sender, receiver, message, context_uid, meta):
        """ Once a new tip is found, do the work. Returns the response from start_transaction """
        self.last_context_uid = context_uid
        self.dupecheck(context_uid)
        return self.start_transaction(sender, receiver, message, context_uid, meta)

    def deliver_tip_response(self, tx):
        """ Does the work to post the response to the thread on the site. Returns True or Exception """
        raise NotImplementedError

    def deliver_tip_confirmation(self, tx):
        """ Does the work to post the confirmation to the thread on the site. Returns True or Exception """
        # Often the email is enough, most bots will just pass
        pass

    def invite_new_user(self, sender, **kwargs):
        """ Invite the sender to create an account on ChangeTip
        :param **kwargs:
        """
        pass

    def missing_amount_message(self, tx, tiplike_text, process=True):
        """ How to interact with the user when there is no amount parsed
        """
        pass

    def send_tip_reminder(self, tx):
        """ A reminder to the receiver that their tip is about to expire """
        pass

    def on_over_tip_limit(self, tx, limit, process=True):
        """ How to interact with the user when there is an tip attempt over the limit
        """
        pass

    def get_api_url(self, path):
        assert self.changetip_api_key is not None, "changetip_api_key must be defined"
        return "%s%s?api_key=%s" % (settings.CHANGECOIN_API, path, self.changetip_api_key)

    def start_transaction(self, sender, receiver, message, context_uid, meta):
        """ Send data to the changecoin API """
        assert self.channel is not None, "channel must be defined"
        data = json.dumps({
            "channel": self.channel,
            "sender": sender,
            "receiver": receiver,
            "message": message,
            "context_uid": context_uid,
            "meta_json": meta,
        })
        response = requests.post(self.get_api_url("/transactions/start"), data=data, headers={'content-type': 'application/json'})
        assert response.status_code in [200, 409], "%s error submitting transaction: %s" % (response.status_code, response.content)
        return response

    def get_mentions(self, message):
        """ Remove duplicates in a case-insensitive way while preserving the original order
            Return all mentions in lower case *without* their prefixes. (So return ['clyde'], not ['@clyde'])
        >>> BaseBot().get_mentions("This is a @user")
        ['user']
        >>> BaseBot().get_mentions("This is empty")
        []
        >>> BaseBot().get_mentions("title case and end of string @mention @ChangeTip. and @")
        ['mention', 'changetip']
        >>> BaseBot().get_mentions("@ This one has an empty one and two @mention-69 @changetip.")
        ['mention-69', 'changetip']
        >>> BaseBot().get_mentions("This one has a dupe @mention-69 @changetip and @mention-69.")
        ['mention-69', 'changetip']
        """
        mentions = re.findall(re.escape(self.prefix) + '([\w-]+)', message)
        mentions_set = set([m.lower() for m in mentions])

        deduped_mentions = []
        for m in mentions:
            m = m.lower()
            if m in mentions_set:
                mentions_set.remove(m)
                deduped_mentions.append(m)

        return deduped_mentions

    def get_sibling_tips(self, parent_id):
        response = requests.get(self.get_api_url("/transactions"), params={"context_parent_uid": parent_id}, headers={'content-type': 'application/json'})
        return response.json()["objects"]