import matplotlib.pyplot as plt
import matplotlib.widgets as mwidgets
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [10, 50, 100])
def onselect(vmin, vmax):
    print(vmin, vmax)
rectprops = dict(facecolor='blue', alpha=0.5)
span = mwidgets.SpanSelector(ax, onselect, 'horizontal',rectprops=rectprops)
fig.show()
