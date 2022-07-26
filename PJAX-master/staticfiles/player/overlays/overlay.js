export class Overlay {
	/**
	 * Тип наложения
	 * @type {string}
	 */
	type;

	/**
	 * Список дополнительных классов для наложения
	 * @type {string[]}
	 */
	classes = [];

	/**
	 * Словарь дополнительных стилей для наложения
	 * @type {Object<string, string>}
	 */
	styles = {};

	/**
	 * Создает новый экземпляр наложения
	 *
	 * @param {{
	 *   type: string,
	 *   classes?: string[],
	 *   styles?: Object<string, string>
	 * }=} [params] - параметры наложения:
	 *
	 * 1. type - тип создаваемого наложения
	 * 2. [classes] - список дополнительных классов
	 * 3. [styles] - список дополнительных стилей
	 */
	constructor(params) {
		this.type = params.type;

		if (typeof this.type !== 'string') {
			throw new TypeError('A type of the created overlay is not specified');
		}

		this.classes = params?.classes ?? this.classes;

		if (!Array.isArray(this.classes)) {
			throw new TypeError('Additional classes can be defined only as array');
		}

		this.styles = params?.styles ?? this.styles;

		if (typeof this.styles !== 'object') {
			throw new TypeError('Additional styles can be defined only as object');
		}
	}

	/**
	 * Рендерит исходный виджет
	 * @returns {Element}
	 */
	render() {
		const
			classes = this.classes.join(' ');

		const styles = Object.entries(this.styles)
			.map((el) => el.join(':'))
			.join(';');

		const tpl = `<div class="player-chunk-overlay ${classes}" style="${styles}"></div>`;

		const wrapper = document.createElement('div');
		wrapper.innerHTML = tpl;

		return wrapper.children[0];
	}
}
