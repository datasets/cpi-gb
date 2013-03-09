var csv = require('csv');

var lookup = {
  'JAN': '01',
  'FEB': '02',
  'MAR': '03',
  'APR': '04',
  'MAY': '05',
  'JUN': '06',
  'JUL': '07',
  'AUG': '08',
  'SEP': '09',
  'OCT': '10',
  'NOV': '11',
  'DEC': '12'
};

function process() {
  var skip = false;
  var outcsv = csv().to.path('data/cpi-uk-annual.csv');
  var outcsv2 = csv().to.path('data/cpi-uk-monthly.csv');
  csv()
    .from.path('cache/cpi-uk.csv')
    .on('record', function(data, idx) {
      if (idx == 0) {
        outcsv.write(['Year','Price Index']);
        outcsv2.write(['Date','Price Index']);
        return;
      } else if (!data[0] || skip) {
        skip = true;
        return;
      }
      var parts = data[0].split(' ');
      if (parts.length > 1) {
        data[0] = parts[0] + '-' + lookup[parts[1]] + '-01';
        outcsv2.write(data);
      } else {
        data[0] = parts[0];
        outcsv.write(data);
      }
    });
}

process();

