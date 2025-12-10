<template>
	<div class="card diff-card" v-if="comparison">
		<h3>Key Differences</h3>
		<div class="chips">
			<span class="chip">Score: {{ comparison.seo_score_diff }}</span>
			<span class="chip">Words: {{ comparison.word_count_diff }}</span>
			<span class="chip">Load: {{ loadTime }}</span>
			<span class="chip">Missing ALTs: {{ comparison.missing_alts_diff }}</span>
			<span class="chip">Internal Links: {{ comparison.internal_links_diff }}</span>
		</div>
	</div>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
	comparison: {
		type: Object,
		default: null,
	},
});

const loadTime = computed(() =>
	props.comparison?.load_time_diff !== undefined && props.comparison?.load_time_diff !== null
		? `${props.comparison.load_time_diff.toFixed(2)}s`
		: '—',
);
</script>

<style scoped>
.diff-card {
	text-align: center;
	display: flex;
	flex-direction: column;
	gap: 8px;
	justify-content: center;
	margin-bottom: 12px;
}

.diff-card h3 {
	margin: 0;
}

.chips {
	display: flex;
	flex-wrap: wrap;
	gap: 8px;
	justify-content: center;
}

.chip {
	background: var(--input-bg);
	border: 1px solid var(--border);
	padding: 6px 12px;
	border-radius: 999px;
	font-size: 13px;
}
</style>
