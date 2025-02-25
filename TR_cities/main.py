from turtle import Screen,Turtle
import turtle
import pandas


#def get_mouse_click_coor(x, y):
#    print(x, y)

#turtle.onscreenclick(get_mouse_click_coor)
#turtle.mainloop()

screen=Screen()
image='../../Downloads/turkiye_haritasi.gif'
t=Turtle()
turtle.addshape(image)
turtle.shape(image)
data=pandas.read_csv('cities_in_TR.csv')
all_cities=data.cities.to_list()
guess=[]
non_guessed=[]
while len(guess)<81:
   answer=screen.textinput(title=f'Guess the city:{len(guess)}/50', prompt='what is another city\'s name').title()
   if answer=='Exit':
        for city in all_cities:
           if city not in guess:
                non_guessed.append(city)
        break

   if answer in all_cities:
      guess.append(answer)
      city=data[data.cities==answer]
      t.penup()
      t.hideturtle()
      t.goto(city.x.item(),city.y.item())
      t.write(answer)

remaining_cities=pandas.DataFrame(non_guessed)
remaining_cities.to_csv('non_guessed_cities.csv')



screen.exitonclick()




