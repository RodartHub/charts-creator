#Because of this module, we can create bar charts with the information of csv's

import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    ax.axis('equal')
    plt.show()

def main():
    labels = ['a', 'b', 'c']
    values = [100, 200, 80]
    # generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)


if __name__ == '__main__':
    main()
    



