import time

class RobotMotorsControl:
    def __init__(self):
        self.motor_speed = 0
        self.is_running = False
        self.max_acceleration = 10  # максимальное ускорение в %/сек
    
    # ... предыдущие методы остаются без изменений ...
    
    def smooth_speed_change(self, target_speed, duration=2.0):
        """Плавное изменение скорости"""
        if not self.is_running:
            print("Ошибка: двигатели не запущены")
            return
        
        if not 0 <= target_speed <= 100:
            print("Ошибка: скорость должна быть от 0 до 100%")
            return
        
        start_speed = self.motor_speed
        steps = int(duration * 10)  # 10 обновлений в секунду
        step_delay = duration / steps
        
        print(f"Плавное изменение скорости с {start_speed}% до {target_speed}%")
        
        for i in range(steps + 1):
            progress = i / steps
            current_speed = start_speed + (target_speed - start_speed) * progress
            self.motor_speed = int(current_speed)
            print(f"Текущая скорость: {self.motor_speed}%")
            time.sleep(step_delay)
        
        print("Изменение скорости завершено")
    
    def handle_user_input(self):
        """Обработка пользовательского ввода"""
        print("\n=== Управление двигателями робота ===")
        print("1 - Запустить двигатели")
        print("2 - Остановить двигатели")
        print("3 - Установить скорость")
        print("4 - Плавное изменение скорости")
        print("5 - Показать статус")
        print("0 - Выход")
        
        while True:
            try:
                choice = input("\nВыберите действие: ")
                
                if choice == '1':
                    self.start_motors()
                elif choice == '2':
                    self.stop_motors()
                elif choice == '3':
                    speed = int(input("Введите скорость (0-100): "))
                    self.set_speed(speed)
                elif choice == '4':
                    if not self.is_running:
                        print("Сначала запустите двигатели!")
                        continue
                    target = int(input("Целевая скорость (0-100): "))
                    duration = float(input("Длительность (сек): ") or "2.0")
                    self.smooth_speed_change(target, duration)
                elif choice == '5':
                    status = self.get_status()
                    print(f"Статус: {'работают' if status['running'] else 'остановлены'}")
                    print(f"Скорость: {status['speed']}%")
                elif choice == '0':
                    print("Выход из программы")
                    break
                else:
                    print("Неверный выбор")
                    
            except ValueError:
                print("Ошибка: введите корректное число")
            except KeyboardInterrupt:
                print("\nПрограмма прервана пользователем")
                break

# Обновленный пример использования
if __name__ == "__main__":
    robot = RobotMotorsControl()
    robot.handle_user_input()
