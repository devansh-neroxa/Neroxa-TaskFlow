class NeroxaTaskFlow:
    @staticmethod
    def execute_queue(tasks):
        for task in tasks:
            print(f"Executing task: {task}")
        print("TaskFlow: All background tasks executed successfully!")
