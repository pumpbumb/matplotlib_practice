import numpy as np
import matplotlib.pyplot as plt

data = {'Barton LLC': 109438.50,
        'Frami, Hills and Schmidt': 103569.59,
        'Fritsch, Russel and Anderson': 112214.71,
        'Jerde-Hilpert': 112591.43,
        'Keeling LLC': 100934.30,
        'Koepp Ltd': 103660.54,
        'Kulas Inc': 137351.96,
        'Trantow-Barrows': 123381.38,
        'White-Trantow': 135841.99,
        'Will LLC': 104437.60}

print(data.values(), '\n')
group_data = list(data.values())
print(type(group_data), '\n', group_data, '\n')

print(data.keys(), '\n')
group_names = list(data.keys())
print(type(group_names), '\n', group_names, '\n')

group_mean = np.mean(group_data)
print(group_mean, '\n')

##########################################################################
"""
There are many styles available in Matplotlib in order to let you tailor your visualization to your needs. 
To see a list of styles, we can use style.
"""
plt.style.use('fivethirtyeight')
plt.rcParams.update({'figure.autolayout': True})

print(plt.style.available)
fig, ax = plt.subplots(num=1, figsize=(8, 4))
ax.barh(group_names, group_data)

labels = ax.get_xticklabels()
print('\n', type(labels))  # <class 'list'>
plt.setp(labels, rotation=45, horizontalalignment='right')

# Add a vertical line across the Axes.
ax.axvline(group_mean, linestyle='--', color='r')

ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company',
       title='Company Revenue')

# Annotate new companies
for group in [3, 5, 8]:
    ax.text(145000, group, "New Company", fontsize=10,
            verticalalignment="center")

plt.show()

##########################################################################
"""
Now that we're happy with the outcome of our plot, we want to save it to disk. 
There are many file formats we can save to in Matplotlib. 
To see a list of available options, use:
"""
print('\n', fig.canvas.get_supported_filetypes())

# save the figure
fig.savefig('sales.png', transparent=False, dpi=80, bbox_inches="tight")
