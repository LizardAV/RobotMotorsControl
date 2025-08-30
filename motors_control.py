class RobotMotorsControl:
    def __init__(self):
        self.motor_speed = 0
        self.is_running = False
    
    def start_motors(self):
        """Запуск двигателей"""
        self.is_running = True
        print("Двигатели запущены")
    
    def stop_motors(self):
        """Остановка двигателей"""
        self.is_running = False
        self.motor_speed = 0
        print("Двигатели остановлены")
    
    def set_speed(self, speed):
        """Установка скорости двигателей"""
        if 0 <= speed <= 100:
            self.motor_speed = speed
            print(f"Скорость установлена: {speed}%")
        else:
            print("Ошибка: скорость должна быть от 0 до 100%")
    
    def get_status(self):
        """Получение статуса двигателей"""
        return {
            'running': self.is_running,
            'speed': self.motor_speed
        }

# Пример использования
if __name__ == "__main__":
    robot = RobotMotorsControl()
    robot.start_motors()
    robot.set_speed(50)
    print(robot.get_status())
    robot.stop_motors()
