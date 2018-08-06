
var		data_raw;
var		data;
var		features;

function	parseData() {
	var		lines;
	var		elem;
	var		set;

	lines = data_raw.split('\n');
	features = lines[0].split(',');
	console.log(features);
	data = new Array();
	for (var i = 1; i < lines.length; i++)
	{
		elem = new Object();
		set = lines[i].split(',');
		for (var j in features)
			elem[features[j]] = set[j];
		data.push(elem);
	}
}

function	onLoad() {
	var		default_data;
	var		file_button;
	var		load_status;
	var		reader = new FileReader();
	var		file;

	file_button = document.getElementById("data");
	load_status = document.getElementById("loadStatus");
	file_button.addEventListener('change', function(e) {
		load_status.innerHTML = "Loading...";

		file = e.srcElement.files[0];
		reader.addEventListener("load", function() {
			data_raw = reader.result;
			load_status.innerHTML = file.name;
			parseData();
		});
		reader.readAsText(file, 'UTF-8');
	});
}
