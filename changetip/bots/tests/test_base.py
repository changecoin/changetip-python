from unittest import TestCase
from changetip.bots.base import BaseBot


class BaseBotTest(TestCase):

    def setUp(self):
        super(BaseBotTest, self).setUp()

        self.tipbot = BaseBot()

    def test_parse_mentions(self):
        tests = [
            ['Check out @ChangeTip, you can send 1 beer to @sarahhagstrom @changetip to send money for a beer!', ['changetip', 'sarahhagstrom']],
            ['@sarahhagstrom have 1 beer on me @ChangeTip', ['sarahhagstrom', 'changetip']],
            ['@Doom_ @doom @DOOM_, @doomy_dooM', ['doom_', 'doom', 'doomy_doom']],
            ['@sarah-hagstrom have 1 beer on me @ChangeTip', ['sarah-hagstrom', 'changetip']],
        ]
        for test in tests:
            self.assertEqual(self.tipbot.get_mentions(test[0]), test[1])
