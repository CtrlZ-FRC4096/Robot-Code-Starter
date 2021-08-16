import wpilib
import wpilib.drive
import wpilib.interfaces


class Robot(wpilib.TimedRobot):
	"""
	Main robot class
	"""
	def robotInit(self):
		self.dt_motor_left = wpilib.VictorSP(0)
		self.dt_motor_right = wpilib.VictorSP(1)
		self.dt_motor_right.setInverted(True)

		self.drive = wpilib.drive.DifferentialDrive(self.dt_motor_left, self.dt_motor_right)

		self.xbox_controller = wpilib.XboxController(0)

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
		forward_val = self.xbox_controller.getY(wpilib.interfaces.GenericHID.Hand.kRightHand)
		rotate_val = self.xbox_controller.getX(wpilib.interfaces.GenericHID.Hand.kLeftHand)
		self.drive.arcadeDrive(forward_val, rotate_val)



### MAIN ###

if __name__ == "__main__":
	wpilib.run(Robot)
