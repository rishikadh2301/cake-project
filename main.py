###MAIN FILE###
from turtle import Screen,Turtle
from Rishika_Dhawan_activity1 import draw_cake,draw_layer,table,legs_table
def main():
    table_size = int(input("Please enter the length of table (between 200 - 400): "))
    max = int(table_size*0.75)
    table_color = input("Please enter the color of the table: ")
    cake_size = int(input(f"Please enter the size of the cake (between 50 - {max}): "))
    color1 = input("Please enter the color of the first layer of the cake: ")
    color2 = input("Please enter the color of the second layer of the cake: ")
    color3 = input("Please enter the color of the third layer of the cake: ")
    color4 = input("Please enter the color of the icing: ")
    print("Happy Birthday!\nClick anywhere on the scene to exit...")

    sc = Screen()
    sc.bgcolor("light blue")
    sc.title("Birthday Scenery")
    turta = Turtle()
    turta.pensize(1)
    turta.speed(0)
    turta.getscreen()._root.attributes("-topmost", True)

    table(0,0,table_size,table_size*1/5,table_color,turta)
    draw_cake(-cake_size/10, -cake_size/20, cake_size, color1, color2, color3, color4, turta)

    turta.hideturtle()
    sc.exitonclick()

main()