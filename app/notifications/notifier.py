class NotificationService:

    def notify(self, execution_summary):
        print("Execution Summary:")
        for order in execution_summary:
            print(order)