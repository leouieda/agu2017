import gmt

fig = gmt.Figure()
fig.pscoast(region='-270/90/-70/70', projection='M10i', land='#dddddd',
            water='white', resolution='l')
fig.savefig('poster_background.png', dpi=1000)
