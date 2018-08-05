
var		datas;

function	onLoad() {
	var		default_data;
	var		default_data_button;
	var		custom_data_button;
	var		load_status;
	var		reader = new FileReader();
	var		file;

	default_data_button = document.getElementById("defaultData");
	custom_data_button = document.getElementById("data");
	load_status = document.getElementById("loadStatus");
	default_data_button.addEventListener('click', function(e) {
		load_status.innerHTML = "Loading...";
		if (default_data === undefined) {
			var request = new XMLHttpRequest();

			request.open("GET", "resources/dataset_train.csv", false);
			request.addEventListener("load", function() {
				if (request.readyState == 4)
				{
					if (request.status == 200 || request.status == 0)
					{
						default_data = request.responseText;
						datas = default_data;
						load_status.innerHTML = "Default data";
					}
				}
			});
			request.send(null);
		}
		else
		{
			datas = default_data;
			load_status.innerHTML = "Default data";
		}
	});
	custom_data_button.addEventListener('change', function(e) {
		load_status.innerHTML = "Loading...";

		file = e.srcElement.files[0];
		reader.addEventListener("load", function() {
			datas = reader.result;
			load_status.innerHTML = file.name;
		});
		data = reader.readAsText(file, 'UTF-8');
	});
}
