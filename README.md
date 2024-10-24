<a href="https://datahub.io/core/cpi-gb"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25)" alt="badge" /></a>

Consumer Price Index (and hence inflation) for the UK from 1850 to the present (monthly since June 1947).

## Data

Key source files are:

* [Price Index 1800 to Present](http://www.ons.gov.uk/ons/datasets-and-tables/downloads/csv.csv?dataset=mm23&cdid=CDKO)
* [Inflation 1800 to Present](http://www.ons.gov.uk/ons/datasets-and-tables/downloads/csv.csv?dataset=mm23&cdid=CDSI)

We take these and just to a split out of annual from monthly and some tidying of the date format (see scripts/process.js).

### Processing

First do:

    curl "http://www.ons.gov.uk/ons/datasets-and-tables/downloads/csv.csv?dataset=mm23&cdid=CDKO" > cache/cpi-uk.csv

Then run the processing script to split out monthly and annual (they put them in the same file ...):

    node scripts/process.js

## Rant

Why is it always so complicated to get data. A quick search on the interwebs yields: <http://www.ons.gov.uk/ons/rel/cpi/consumer-price-indices/october-2012/cpi-time-series-data.html>

But this turns out to be so big that it does not open in a spreadsheet programme (if you take CSV). In addition all the series descriptions are mixed in at the bottom of the file so this is not machine processable!

Let's try instead to go for the series selector to try and break it down: <http://www.ons.gov.uk/ons/datasets-and-tables/data-selector.html?dataset=mm23>

But this is about 20 different series - which one do you want? Make an educated guess and repeat each time you're wrong!

