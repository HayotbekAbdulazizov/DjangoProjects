export default class ClassSwitcher {
	/**
	 * Корневой элемент
	 * @type {Element}
	 */
	root;

	/**
	 * Идентификатор таймера
	 * @type {number|undefined}
	 */
	timelineTimer;

	/**
	 * @param {Element} root - корневой элемент
	 */
	constructor(root) {
		this.root = root;

		if (!(this.root instanceof Element)) {
			throw new TypeError('The root element is not defined');
		}
	}

	moveClass(className, method, pred) {
		const
			active = this.root.querySelector('.' + className),
			next = active[method];

		if (pred && !pred(active)) {
			return null;
		}

		if (next) {
			active.classList.remove(className);
			next.classList.add(className);

			return active;
		}

		return null;
	}

	switchToPrevChunk() {
		this.moveClass('player-chunk-active', 'previousElementSibling');
		this.moveClass('timeline-chunk-active', 'previousElementSibling', (el) => {
			const
				inner = el.querySelector('.timeline-chunk-inner'),
				w = parseFloat(inner.style.width) || 0;

			el.querySelector('.timeline-chunk-inner').style.width = '';
			return w <= 20;
		});
	}

	switchToNextChunk() {
		this.moveClass('player-chunk-active', 'nextElementSibling');

		const
			el = this.moveClass('timeline-chunk-active', 'nextElementSibling');

		if (el) {
			el.querySelector('.timeline-chunk-inner').style.width = '';
		}
	}

	runChunkSwitching(time, step) {
		clearInterval(this.timelineTimer);

		this.timelineTimer = setInterval(() => {
			const
				active = this.root.querySelector('.timeline-chunk-active').querySelector('.timeline-chunk-inner');

			const
				w = parseFloat(active.style.width) || 0;

			if (w === 100) {
				this.switchToNextChunk();
				return;
			}

			active.style.width = String(w + step) + '%';

		}, time * 1000 * step / 100);
	}
}
