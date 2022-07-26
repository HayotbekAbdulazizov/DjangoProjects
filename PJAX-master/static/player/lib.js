import ClassSwitcher from './class-switcher.js';

import { Overlay } from './overlays/overlay.js';
import * as overlays from './overlays/index.js';

/**
 * @typedef {{url: string, alt?: string, overlays?: Overlay[]}}
 */
const Slide = null;

/**
 * @typedef {Slide[]}
 */
const Slides = null;

export default class Player {
	/**
	 * Контейнер для плеера
	 * @type {Element}
	 */
	target;

	/**
	 * Список слайдов плеер-а
	 * @type {Slides}
	 */
	slides;

	/**
	 * Как долго показывается один слайд
	 * @type {number}
	 */
	delayPerSlide = 1;

	/**
	 * Экземпляр ClassSwitcher
	 * @protected
	 */
	cs;

	/**
	 * Создает объект плеера
	 *
	 * @param {{
	 *   target: string,
	 *   delayPerSlide?: number,
	 *   slides: Slides
	 * }} params - параметры инициализации:
	 *
	 *  1. target - место инициализации плеер-а, CSS селектор
	 *  2. delayPerSlide - как долго показывается один слайд
	 *  3. slides - список слайдов плеер-а
	 */
	constructor(params) {
		this.target = document.querySelector(params?.target);

		if (this.target == null) {
			throw new ReferenceError('A target to mount the player is not specified');
		}

		this.slides = params?.slides;

		if (!Array.isArray(this.slides)) {
			throw new TypeError('Slides to render is not specified');
		}

		this.delayPerSlide = params?.delayPerSlide ?? this.delayPerSlide;
		this.cs = new ClassSwitcher(this.target);

		this.mount();
	}

	/**
	 * Монтирует элементы плеера к target
	 */
	mount() {
		this.target.appendChild(this.generatePlayerLayout());

		this.target.querySelector('.player-chunk-prev').addEventListener('click', this.cs.switchToPrevChunk.bind(this.cs));
		this.target.querySelector('.player-chunk-next').addEventListener('click', this.cs.switchToNextChunk.bind(this.cs));

		this.cs.runChunkSwitching(this.delayPerSlide, 1);
	}

	/**
	 * Генерирует элементы временной шкалы
	 * @returns {DocumentFragment}
	 */
	generateTimelineChunks() {
		const
			wrapper = document.createDocumentFragment();

		for (const i of this.slides.keys()) {
			const el = document.createElement('div');

			el.innerHTML = `
<div class="timeline-chunk ${i === 0 ? 'timeline-chunk-active' : ''}">
	<div class="timeline-chunk-inner"></div>
</div>`;

			wrapper.appendChild(el.children[0]);
		}

		return wrapper;
	}

	/**
	 * Генерирует элементы слайдов
	 * @returns {DocumentFragment}
	 */
	generatePlayerChunks() {
		const
			wrapper = document.createDocumentFragment();

		for (const [i, slide] of this.slides.entries()) {
			const
				style = [];

			if (slide.filter) {
				style.push(`filter: ${slide.filter.join(' ')}`);
			}

			const el = document.createElement('div');

			el.innerHTML = `
<div class="player-chunk ${i === 0 ? 'player-chunk-active' : ''}">
	<img src="${slide.url}" alt="${slide.alt ?? ''}" style="${style.join(';')}">
</div>`;

			const chunk = el.children[0];
			chunk.appendChild(this.generateOverlays(slide));

			wrapper.appendChild(chunk);
		}

		return wrapper;
	}

	/**
	 * Генерирует элементы наложения на слайд
	 *
	 * @param {Slide} slide - объект слайда
	 * @returns {DocumentFragment}
	 */
	generateOverlays(slide) {
		const wrapper = document.createDocumentFragment();

		if (slide.overlays == null) {
			return wrapper;
		}

		for (const params of slide.overlays) {
			if (!(params.type in overlays)) {
				throw new TypeError(`The specified type of overlay (${params.type}) is not defined`);
			}

			const overlay = new overlays[params.type](params);
			wrapper.appendChild(overlay.render());
		}

		return wrapper;
	}

	/**
	 * Генерирует элементы плеера
	 * @returns {Element}
	 */
	generatePlayerLayout() {
		const timeline = document.createElement('div');

		timeline.setAttribute('class', 'timeline');
		timeline.appendChild(this.generateTimelineChunks());

		const content = document.createElement('div');

		content.setAttribute('class', 'player-content');
		content.appendChild(this.generatePlayerChunks());

		const contentWrapper = document.createElement('div');

		contentWrapper.setAttribute('class', 'player-content-wrapper');
		contentWrapper.innerHTML = `
<div class="player-chunk-switcher player-chunk-prev"></div>
<div class="player-chunk-switcher player-chunk-next"></div>
`;

		contentWrapper.appendChild(content);

		const player = document.createElement('div');

		player.setAttribute('class', 'player');
		player.appendChild(timeline);
		player.appendChild(contentWrapper);

		return player;
	}
}
