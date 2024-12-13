print('đinh văn thiện msv 235752021610032')
import turtle
window = turtle.Screen()
window.bgcolor('white')
thinh = turtle.Turtle()
thinh.pensize(1)
def draw_circle(radius, color):
    thinh.color(color)
    thinh.circle(radius)

num_circles = 60
angle= 30
for i in range(num_circles):
    radius = 50
    color= 'red' if i % 3 == 0 else 'green' if i % 3 ==1 else 'blue'
    draw_circle(radius, color)
    thinh.right(angle)

turtle.done()
    
