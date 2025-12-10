import { onMounted, watch } from 'vue';

export function useDarkMode() {
	const darkMode = useState<boolean>('darkMode', () => false);

	const applyPreference = (enabled: boolean) => {
		if (!process.client) return;
		document.documentElement.classList.toggle('dark', enabled);
		localStorage.setItem('darkMode', enabled ? 'true' : 'false');
	};

	onMounted(() => {
		if (!process.client) return;
		const saved = localStorage.getItem('darkMode');
		if (saved === 'true') {
			darkMode.value = true;
		}
		applyPreference(darkMode.value);
	});

	watch(darkMode, (value) => {
		applyPreference(value);
	});

	const toggleDarkMode = () => {
		darkMode.value = !darkMode.value;
	};

	return { darkMode, toggleDarkMode };
}
