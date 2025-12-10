<template>
	<div class="score-row">
		<div
			class="card score-card primary"
			:class="mainScore > competitorScore ? 'goodLine' : 'badLine'"
		>
			<div class="score-info">
				<p class="eyebrow">Primary</p>
				<h3 class="site-title">{{ mainUrl }}</h3>
			</div>
			<div class="score-number">
				<div class="score-value">
					{{ mainScore ?? '—' }}
				</div>
				<div class="score-label">SEO Score</div>
			</div>
		</div>
		<div
			class="card score-card competitor"
			:class="competitorScore > mainScore ? 'goodLine' : 'badLine'"
		>
			<div class="score-number">
				<div class="score-value">{{ competitorScore ?? '—' }}</div>
				<div class="score-label">SEO Score</div>
			</div>
			<div class="score-info">
				<p class="eyebrow">Competitor</p>
				<h3 class="site-title">{{ competitorUrl }}</h3>
			</div>
		</div>
	</div>
</template>

<script setup>
defineProps({
	mainUrl: {
		type: String,
		default: '',
	},
	competitorUrl: {
		type: String,
		default: '',
	},
	mainScore: {
		type: Number,
		default: null,
	},
	competitorScore: {
		type: Number,
		default: null,
	},
});
</script>

<style scoped>
.goodLine {
	border-bottom: 10px solid var(--good);
}

.badLine {
	border-bottom: 10px solid var(--bad);
}
.score-row {
	display: grid;
	grid-template-columns: repeat(2, minmax(0, 1fr));
	gap: 16px;
	margin-bottom: 12px;
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
	text-align: right;
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

.eyebrow {
	font-size: 12px;
	color: var(--text);
	opacity: 0.7;
	text-transform: uppercase;
	letter-spacing: 0.08em;
}

.site-title {
	font-size: 16px;
	font-weight: 700;
	word-break: break-word;
	line-height: 1.3;
}

.score-value {
	font-size: 32px;
	font-weight: 800;
	line-height: 1.2;
}

.score-label {
	text-align: center;
	color: var(--text);
	font-size: 13px;
	opacity: 0.8;
}
</style>
