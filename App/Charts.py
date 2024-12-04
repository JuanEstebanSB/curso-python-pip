import matplotlib.pyplot as plt

def generate_bar(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig('bar.png')
    plt.close()

def generate_pie(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.savefig('circle.png')
    plt.close()

if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [100, 300, 300]
    generate_bar(labels, values)
    generate_pie(labels, values)

