super().__init__()
        self.ht()
        self.color("white")
        self.shape("square")
        self.speed(0)
        self.penup()
        self.resizemode("user")
        self.shapesize(stretch_len=c.LEN_OF_THE_TURTLE)
        self.tilt(90)
        self.setx(-400)
        self.st()

    def up(self):
        self.setheading(c.HEADINGS[0])

    def down(self):
        self.setheading(c.HEADINGS[1])

    def move(self):
        self.fd(10)
