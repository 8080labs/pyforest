define(['lodash', '@jupyter-widgets/base', '../package.json'], function (_, widgets, package_) {
	function makeWidget(getFirstCellContent, setFirstCellContent) {
		const PyforestWidget = widgets.DOMWidgetView.extend({
			render: function () {
				const content = getFirstCellContent();
				setFirstCellContent(updateImports(this.model.get('imports'), content));
			}
		});
		
		const PyforestWidgetModel = widgets.DOMWidgetModel.extend({
			defaults: _.extend(widgets.DOMWidgetModel.prototype.defaults(), {
				_model_name: 'PyforestWidgetModel',
				_view_name: 'PyforestWidget',
				_model_module: package_.name,
				_view_module: package_.name,
				_model_module_version: package_.version,
				_view_module_version: package_.version,
				imports: []
			})
		});
		
		return {
			PyforestWidget: PyforestWidget,
			PyforestWidgetModel: PyforestWidgetModel
		};
	}
	
	function updateImports(imports, currentContent) {
		const sep = '# ^^^ pyforest imports ^^^';
		let parts = currentContent.split(sep);
		if (parts.length > 1) {
			parts = parts.splice(1);
		}
		return imports.join('\n') + '\n' + sep + '\n' + parts.join('\n').trim('\n');
	}
	
	return {
		makeWidget: makeWidget
	};
});
