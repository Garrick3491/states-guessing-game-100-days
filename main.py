import turtle

import pandas


states = pandas.read_csv('./50_states.csv')

screen = turtle.Screen()
screen.title('U.S. States Game')
image = './blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
correct = []
answer_states = states.state.to_list()
while len(correct) < 50:

    answer_state = screen.textinput(title=f"{len(correct)}/50 States Correct", prompt="Whats another state's name").title()

    if answer_state == 'Exit':
        missing_states = [state for state in answer_states if state not in correct]
        missing_data = pandas.DataFrame(missing_states)
        missing_data.to_csv('states_to_learn.csv')
        break
    if answer_state in answer_states:
        writer = turtle.Turtle()
        writer.penup()
        writer.hideturtle()
        correct.append(answer_state)
        df = states[states.state == answer_state]
        writer.goto(int(df.x), int(df.y))
        writer.write(answer_state)
        # (get_mouse_click_coords)
    print(len(correct))