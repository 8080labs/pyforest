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
	
	const begin = '# begin pyforest imports';
	const end = '# end pyforest imports';
	const any = '[\\s\\S]*';
	const importRegex = new RegExp([
		'^(', any, ')', begin, '\n', any, end, '(', any, ')$'
	].join(''), 'mi');
	
	function updateImports(imports, currentContent) {
		let match = currentContent.match(importRegex);
		if (match == null) {
			match = ['', currentContent, ''];
		}
		if (match[1].length > 0 && match[1].substr(-1) != '\n') {
			match[1] += '\n'
		}
		return [match[1], begin + '\n', imports.join('\n') + '\n', end, match[2]].join('');
	}
	
	return {
		makeWidget: makeWidget
	};
});
