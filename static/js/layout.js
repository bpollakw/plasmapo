var app = angular.module('app', ["angularplasmid"]);
//socket = io();
downloadFrame = document.createElement('iframe');

$(function () {
	downloadFrame.style.display = 'none';
	document.body.appendChild(downloadFrame);

	$('#layout').w2layout({
		name: 'layout',
		panels: [
			{ type: 'preview', size: '100%', resizable: true}
		]
	});
	$("#layout_layout_panel_preview").attr("ng-controller", "preview");
	$("#layout_layout_panel_preview .w2ui-panel-content").attr("ng-include", "url");
	
	angular.element( function() {
		angular.bootstrap( document, ['app'] );
	});
});