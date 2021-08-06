import wpilib


class Robot(wpilib.TimedRobot):
	"""
	Main robot class
	"""
	def robotInit(self):
		pass


	def robotPeriodic(self):
		pass


	def disabledInit(self):
		pass


	def disabledPeriodic(self):
		pass


	def autonomousInit(self):
		pass

	def autonomousPeriodic(self):
		pass


	def teleopInit(self):
		pass


	def teleopPeriodic(self):
		pass



### MAIN ###

if __name__ == "__main__":
	wpilib.run(Robot)
