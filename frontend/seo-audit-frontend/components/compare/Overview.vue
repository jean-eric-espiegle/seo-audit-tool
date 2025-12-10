<template>
	<div class="card overview-card">
		<div class="overview-row">
			<div>
				<p class="eyebrow">Primary</p>
				<h3>{{ mainUrl }}</h3>
			</div>
			<div class="vs-pill">vs</div>
			<div>
				<p class="eyebrow">Competitor</p>
				<h3>{{ competitorUrl }}</h3>
			</div>
		</div>
		<p class="muted">
			Quick look at the side-by-side comparison across key SEO signals.
		</p>
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
});
</script>

<style scoped>
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
	text-align: center;
}

@media (max-width: 720px) {
	.overview-row {
		justify-content: center;
		text-align: center;
	}

	.vs-pill {
		margin: 6px 0;
	}
}
</style>
