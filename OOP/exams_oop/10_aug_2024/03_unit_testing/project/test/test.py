from multiprocessing.dummy import JoinableQueue

from project.soccer_player import SoccerPlayer

from unittest import TestCase, main
class TestSoccerPlayer(TestCase):
    def setUp(self):
        self.player = SoccerPlayer("John Doe", 32, 180, 'Barcelona')

    def test_init(self):
        self.assertEqual("John Doe", self.player.name)
        self.assertEqual(32, self.player.age)
        self.assertEqual(180, self.player.goals)
        self.assertEqual('Barcelona', self.player.team)
        self.assertEqual({}, self.player.achievements)

    def test_set_name_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.player.name = "John"
        self.assertEqual("Name should be more than 5 symbols!", str(ex.exception))

    def test_set_age_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.player.age = 15
        self.assertEqual("Players must be at least 16 years of age!", str(ex.exception))

    def test_set_goals_when_negative(self):
        self.player.goals = -1
        self.assertEqual(0, self.player.goals)

    def test_set_team_when_not_valid_raises_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.player.team = "Invalid Team"
            self.assertEqual('Team must be one of the following: '
                             '"Barcelona", "Real Madrid", "Manchester United", "Juventus", "PSG"!', str(ex.exception))


    def test_change_team_not_valid_team_name(self):
        result = self.player.change_team("Some Fake Club")
        self.assertEqual("Invalid team name!", result)
        self.assertNotEqual("Some Fake Club", self.player.team)
        # Reset team for other tests

    def test_change_team_valid_team_name(self):
        result = self.player.change_team("Real Madrid")
        self.assertEqual("Team successfully changed!", result)
        self.assertEqual("Real Madrid", self.player.team)

    def test_add_new_achievement_in(self):
        result = self.player.add_new_achievement("New Achievement 1")
        self.assertIn("New Achievement 1", self.player.achievements)
        self.assertEqual(1, len(self.player.achievements))
        self.assertEqual("New Achievement 1 has been successfully added to the achievements collection!", result)

    def test_add_new_achievement_duplicate(self):
        self.player.add_new_achievement("New Achievement 1")
        result = self.player.add_new_achievement("New Achievement 1")
        self.assertEqual(result, "New Achievement 1 has been successfully added to the achievements collection!")
        self.assertEqual(self.player.achievements["New Achievement 1"], 2)

    def test_add_new_achievement_first_time(self):
        result = self.player.add_new_achievement("Python Pro")
        self.assertEqual("Python Pro has been successfully added to the achievements collection!", result)
        self.assertEqual(1, self.player.achievements["Python Pro"])

    def test_add_same_achievement_multiple_times(self):
        self.player.add_new_achievement("Bug Hunter")
        self.player.add_new_achievement("Bug Hunter")
        self.assertEqual(2, self.player.achievements["Bug Hunter"])
        self.assertEqual("Bug Hunter has been successfully added to the achievements collection!",
                         self.player.add_new_achievement("Bug Hunter"))

    def test_less_than_goal(self):
        other_player = SoccerPlayer("Leo Messi", 36, 200, "Barcelona")

        result = self.player < other_player
        expected = "Leo Messi is a top goal scorer! S/he scored more than John Doe."
        self.assertEqual(expected, result)

        # Test when self has more goals than other
        self.player.goals = 300
        result = self.player < other_player
        expected = "John Doe is a better goal scorer than Leo Messi."
        self.assertEqual(expected, result)

if __name__ == "__main__":
    main()