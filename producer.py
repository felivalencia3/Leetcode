"""
Write a producer class, which takes messages and sends them to a pre-defined network endpoint. Contraints:

The class should have some caching in place, that it should not try to send message as it gets them.
The class will be instantiated from a single process. The instance may be shared across multiple processes.
The constructor should take 2 arguments
First argument should be the max count of messages. At any instant producer cannot hold more messages that this count.
Second argument should be the "max time allowed for each message to be held". At any instant, the producer cannot hold any message to time more than this argument.
The class should expose a public "SendMessage" API which takes a string as a message, and sends it.

"""


class Producer:
    def __init__(self, max_count, max_time):
        self.max_count = max_count
        self.max_time = max_time
        self.queue = []
        self.time = []
        self.count = 0
    def SendMessage(self, message):
        if self.count < self.max_count:
            self.queue.append(message)
            self.time.append(time.time())
            self.count += 1
        else:
            if time.time() - self.time[0] > self.max_time:
                self.queue.pop(0)
                self.time.pop(0)
                self.queue.append(message)
                self.time.append(time.time())
            else:
                print("Queue is full")
    def __str__(self):
        return str(self.queue)
