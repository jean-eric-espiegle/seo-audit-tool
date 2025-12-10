<template>
	<div>
		<LazyNavBar />

		<div class="container compare-page">
			<h1 class="page-title">SEO Competitor Comparison</h1>
			<p class="page-subtitle">
				Compare two sites side by side across SEO, content, links, and performance.
			</p>

			<LazyCompareForm
				:url1="url1"
				:url2="url2"
				:loading="loading"
				@update:url1="(v) => (url1 = v)"
				@update:url2="(v) => (url2 = v)"
				@submit="runCompare"
			/>

			<p v-if="error" class="error">{{ error }}</p>

			<div v-if="result" class="result-block">
				<LazyCompareOverview
					:main-url="result.main?.url || url1"
					:competitor-url="result.competitor?.url || url2"
				/>

				<LazyCompareScores
					:main-url="result.main?.url || url1"
					:competitor-url="result.competitor?.url || url2"
					:main-score="result.main?.seo_score"
					:competitor-score="result.competitor?.seo_score"
				/>

				<LazyCompareDifferences :comparison="result.comparison" />

				<div class="grid grid-2">
					<LazyCompareTable
						class="full-span"
						title="Content"
						:main-header="result.main?.url || url1"
						:competitor-header="result.competitor?.url || url2"
						:rows="contentRows"
					/>

					<LazyCompareTable
						title="Links & Accessibility"
						:main-header="formatDomain(result.main?.url || url1)"
						:competitor-header="formatDomain(result.competitor?.url || url2)"
						:rows="linkRows"
					/>

					<LazyCompareTable
						title="Performance"
						:main-header="formatDomain(result.main?.url || url1)"
						:competitor-header="formatDomain(result.competitor?.url || url2)"
						:rows="performanceRows"
					/>

					<LazyCompareKeywords
						:main-url="formatDomain(result.main?.url || url1)"
						:competitor-url="formatDomain(result.competitor?.url || url2)"
						:main-keywords="result.main?.keywords"
						:competitor-keywords="result.competitor?.keywords"
					/>

					<LazyCompareBrokenLinks
						:main-url="formatDomain(result.main?.url || url1)"
						:competitor-url="formatDomain(result.competitor?.url || url2)"
						:main-broken="result.main?.broken_links"
						:competitor-broken="result.competitor?.broken_links"
					/>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed } from 'vue';

// ensure saved dark mode preference is applied globally
useDarkMode();

const { public: publicConfig } = useRuntimeConfig();

const url1 = ref('');
const url2 = ref('');
const loading = ref(false);
const error = ref('');
const result = ref(null);

const runCompare = async () => {
	error.value = '';
	result.value = null;
	loading.value = true;

	try {
		const res = await $fetch(`${publicConfig.apiBase}/seo-compare`, {
			method: 'GET',
			params: {
				url1: url1.value,
				url2: url2.value,
			},
		});

		// FastAPI returns whatever audit_competitor returns; store it directly
		result.value = res;
	} catch (e) {
		error.value =
			e?.data?.detail ||
			e?.message ||
			'Failed to run comparison. Please try again.';
	} finally {
		loading.value = false;
	}
};

function formatSeconds(value) {
	if (value === null || value === undefined) return '—';
	return `${value.toFixed(2)}s`;
}

function formatBytes(bytes) {
	if (!bytes && bytes !== 0) return '—';
	if (bytes < 1024) return `${bytes} B`;
	if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`;
	return `${(bytes / (1024 * 1024)).toFixed(1)} MB`;
}

function prettyBool(val) {
	if (val === undefined || val === null) return '—';
	return val ? 'Yes' : 'No';
}

function formatDomain(value) {
	if (!value) return '—';
	try {
		const url = new URL(value.startsWith('http') ? value : `https://${value}`);
		const host = url.hostname;
		return host.replace(/^www\./, '').split('.').slice(0, -1).join('.') || host.replace(/^www\./, '');
	} catch {
		return value.replace(/^https?:\/\//, '').replace(/^www\./, '');
	}
}

const contentRows = computed(() => {
	if (!result.value) return [];
	return [
		{ label: 'Title', main: result.value.main?.title || '—', competitor: result.value.competitor?.title || '—' },
		{
			label: 'Description',
			main: result.value.main?.meta_description || '—',
			competitor: result.value.competitor?.meta_description || '—',
		},
		{ label: 'H1', main: result.value.main?.h1 || '—', competitor: result.value.competitor?.h1 || '—' },
		{ label: 'Word Count', main: result.value.main?.word_count ?? '—', competitor: result.value.competitor?.word_count ?? '—' },
		{
			label: 'Viewport Meta',
			main: prettyBool(result.value.main?.has_viewport_tag),
			competitor: prettyBool(result.value.competitor?.has_viewport_tag),
		},
	];
});

const linkRows = computed(() => {
	if (!result.value) return [];
	return [
		{ label: 'Internal Links', main: result.value.main?.internal_links, competitor: result.value.competitor?.internal_links },
		{ label: 'External Links', main: result.value.main?.external_links, competitor: result.value.competitor?.external_links },
		{ label: 'Missing ALTs', main: result.value.main?.missing_image_alts, competitor: result.value.competitor?.missing_image_alts },
		{
			label: 'Robots.txt',
			main: prettyBool(result.value.main?.robots_txt_found),
			competitor: prettyBool(result.value.competitor?.robots_txt_found),
		},
		{
			label: 'Sitemap',
			main: prettyBool(result.value.main?.sitemap_found),
			competitor: prettyBool(result.value.competitor?.sitemap_found),
		},
	];
});

const performanceRows = computed(() => {
	if (!result.value) return [];
	return [
		{
			label: 'Load Time',
			main: formatSeconds(result.value.main?.load_time_seconds),
			competitor: formatSeconds(result.value.competitor?.load_time_seconds),
		},
		{
			label: 'Page Size',
			main: formatBytes(result.value.main?.performance?.page_size_bytes),
			competitor: formatBytes(result.value.competitor?.performance?.page_size_bytes),
		},
		{
			label: 'Scripts',
			main: result.value.main?.performance?.script_count,
			competitor: result.value.competitor?.performance?.script_count,
		},
		{
			label: 'Images',
			main: result.value.main?.performance?.image_count,
			competitor: result.value.competitor?.performance?.image_count,
		},
		{
			label: 'DOM Nodes',
			main: result.value.main?.performance?.dom_nodes,
			competitor: result.value.competitor?.performance?.dom_nodes,
		},
	];
});
</script>

<style scoped>
.compare-page {
	max-width: 1100px;
	margin: 0 auto;
	padding-bottom: 32px;
}

.page-title {
	font-size: 32px;
	font-weight: 800;
	text-align: center;
	margin-bottom: 10px;
}

.page-subtitle {
	text-align: center;
	color: var(--text);
	margin-bottom: 24px;
}

.compare-form {
	margin-bottom: 20px;
}

.overview-card {
	margin-bottom: 20px;
}

.overview-row {
	display: flex;
	justify-content: space-between;
	align-items: center;
	gap: 12px;
	flex-wrap: wrap;
}

.vs-pill {
	background: var(--primary);
	color: #fff;
	padding: 8px 12px;
	border-radius: 999px;
	font-weight: 700;
	text-transform: uppercase;
	letter-spacing: 0.05em;
}

.eyebrow {
	font-size: 12px;
	color: var(--text);
	opacity: 0.7;
	text-transform: uppercase;
	letter-spacing: 0.08em;
	margin-bottom: 4px;
}

.muted {
	color: var(--text);
	opacity: 0.8;
	margin-top: 8px;
}

.form-row {
	display: grid;
	grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
	gap: 16px;
	align-items: end;
}

.field {
	display: flex;
	flex-direction: column;
	gap: 6px;
}

.error {
	color: #c62828;
	margin-bottom: 16px;
}

.result-block {
	margin-top: 24px;
}

.score-row {
	display: grid;
	grid-template-columns: repeat(2, minmax(0, 1fr));
	gap: 16px;
	margin-bottom: 16px;
	align-items: stretch;
}

.score-card {
	display: flex;
	align-items: center;
	justify-content: space-between;
	gap: 12px;
}

.score-card.primary {
	flex-direction: row;
}

.score-card.competitor {
	flex-direction: row-reverse;
}

.score-info {
	display: flex;
	flex-direction: column;
	gap: 4px;
	text-align: left;
}

.score-card.competitor .score-info {
	text-align: right;
	align-items: flex-end;
}

.score-number {
	display: flex;
	flex-direction: column;
	align-items: center;
	min-width: 80px;
}

.score-label {
	text-align: center;
	color: var(--text);
	font-size: 13px;
	opacity: 0.8;
}

.diff-card {
	text-align: center;
	display: flex;
	flex-direction: column;
	gap: 8px;
	justify-content: center;
}

.site-title {
	font-size: 16px;
	font-weight: 700;
	word-break: break-word;
	line-height: 1.3;
}

.grid-2 {
	grid-template-columns: repeat(2, minmax(0, 1fr));
	gap: 18px;
}

.full-span {
	grid-column: 1 / -1;
}

.tags {
	display: flex;
	flex-wrap: wrap;
	gap: 8px;
}

@media (max-width: 720px) {
	.full-span {
		grid-column: 1;
	}

	.grid-2 {
		grid-template-columns: 1fr;
	}
}
</style>
