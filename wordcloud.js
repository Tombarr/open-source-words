// modified from https://github.com/jasondavies/d3-cloud/blob/master/examples/browserify.js

var fill = d3.scaleOrdinal(d3.schemeCategory20);

var baseFontSize = 196;
var fontFamily = '-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol"';

function render(words) {
  var highestFrequency = Math.max(...Object.values(words));
  var layout = d3.layout.cloud()
      .size([document.body.clientWidth, document.body.clientHeight])
      .words(Object.keys(words).map(function(word) {
        return {text: word, size: Math.round(baseFontSize * words[word] / highestFrequency)};
      }))
      .padding(5)
      .rotate(function() { return ~~(Math.random() * 2) * 90; })
      .font(fontFamily)
      .fontSize(function(d) { return d.size; })
      .on("end", draw);

  layout.start();

  function draw(words) {
    d3.select("body").append("svg")
        .attr("width", layout.size()[0])
        .attr("height", layout.size()[1])
      .append("g")
        .attr("transform", "translate(" + layout.size()[0] / 2 + "," + layout.size()[1] / 2 + ")")
      .selectAll("text")
        .data(words)
      .enter().append("text")
        .style("font-size", function(d) { return d.size + "px"; })
        .style("font-family", fontFamily)
        .style("fill", function(d, i) { return fill(i); })
        .attr("text-anchor", "middle")
        .attr("transform", function(d) {
          return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
        })
        .text(function(d) { return d.text; });
  }
}

fetch('./bigram_words.json')
  .then(function(response) {
    return response.json();
  })
  .then(function(words) {
    render(words);
  });
