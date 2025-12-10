<template>
	<section class="card table-card">
		<div class="section-header">
			<h2>{{ title }}</h2>
		</div>
		<div class="comparison-table">
			<div class="table-row table-head">
				<div class="table-label">Metric</div>
				<div class="table-value">{{ mainHeader }}</div>
				<div class="table-value">{{ competitorHeader }}</div>
			</div>
			<div class="table-row" v-for="row in rows" :key="row.label">
				<div class="table-label">{{ row.label }}</div>
				<div class="table-value">{{ row.main }}</div>
				<div class="table-value">{{ row.competitor }}</div>
			</div>
		</div>
	</section>
</template>

<script setup>
defineProps({
	title: {
		type: String,
		required: true,
	},
	mainHeader: {
		type: String,
		default: '',
	},
	competitorHeader: {
		type: String,
		default: '',
	},
	rows: {
		type: Array,
	default: () => [],
	},
});
</script>

<style scoped>
.section-header h2 {
	margin-bottom: 12px;
}

.comparison-table {
	display: grid;
	gap: 6px;
}

.table-row {
	display: grid;
	grid-template-columns: minmax(120px, 160px) 1fr 1fr;
	gap: 10px;
	align-items: start;
	padding: 8px 10px;
	border-radius: 10px;
}

.table-row:nth-child(odd):not(.table-head) {
	background: var(--input-bg);
	border: 1px solid var(--border);
}

.table-head {
	font-weight: 700;
	background: var(--card-bg);
	border: 1px solid var(--border);
}

.table-label {
	font-weight: 600;
}

.table-value {
	color: var(--text);
	word-break: break-word;
	line-height: 1.4;
}

@media (max-width: 720px) {
	.table-row {
		grid-template-columns: 1fr;
	}
}
</style>
