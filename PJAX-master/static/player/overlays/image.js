import { Overlay } from './overlay.js';

export class Image extends Overlay {
	/**
	 * Путь к изображению
	 * @type {string}
	 */
	src;

	/**
	 * Альтернативный текст изображения
	 * @type {string}
	 */
	alt = '';

	/**
	 * @override
	 * @param {{
	 *   type: string,
	 *   src: string,
	 *   alt?: string,
	 *   classes?: string[],
	 *   styles?: Object<string, string>,
	 * }=} [params] - параметры наложения:
	 *
	 * 1. src - путь к изображению
	 * 2. [alt] - альтернативный текст изображения
	 */
	constructor(params) {
		super(params);

		this.src = params?.src;

		if (typeof this.src !== 'string') {
			throw new ReferenceError('URL to the created image overlay is not specified');
		}

		this.alt = params?.alt ?? this.alt;
	}

	/** @override */
	render() {
		const el = super.render();

		el.innerHTML = `<img src="${this.src}" alt="${this.alt}">`;

		return el;
	}
}
