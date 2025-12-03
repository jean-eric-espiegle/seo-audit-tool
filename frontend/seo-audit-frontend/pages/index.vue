<template>
	<div>
		<!-- NAVBAR -->
		<nav class="navbar">
			<div class="nav-title">SEO Audit Tool</div>
			<button class="toggle-btn" @click="toggleDark">
				{{ darkMode ? '🌞 Light Mode' : '🌙 Dark Mode' }}
			</button>
		</nav>

		<div class="container">
			<!-- HEADER -->
			<h1
				style="
					font-size: 40px;
					font-weight: 800;
					text-align: center;
					margin-bottom: 12px;
				"
			>
				SEO Audit Tool
			</h1>

			<p
				style="
					text-align: center;
					color: var(--text);
					margin-bottom: 40px;
					font-size: 17px;
				"
			>
				Analyze website SEO, structure, broken links, performance & more.
			</p>

			<!-- INPUT -->
			<div style="display: flex; gap: 14px; margin-bottom: 30px">
				<input v-model="url" class="input" placeholder="https://example.com" />
				<button class="btn" @click="runAudit" :disabled="loading">
					{{ loading ? 'Scanning…' : 'Analyze' }}
				</button>
			</div>

			<!-- ERROR -->
			<div
				v-if="error"
				class="bad"
				style="text-align: center; margin-bottom: 20px"
			>
				{{ error }}
			</div>

			<!-- RESULTS -->
			<div v-if="result">
				<!-- SCORE -->
				<div class="card" style="text-align: center">
					<h2 style="font-size: 24px; margin-bottom: 20px">SEO Score</h2>

					<div class="score-wrapper">
						<svg width="170" height="170">
							<circle
								cx="85"
								cy="85"
								r="70"
								stroke="#e5e7eb"
								stroke-width="14"
								fill="none"
							/>
							<circle
								cx="85"
								cy="85"
								r="70"
								:stroke="scoreColor"
								stroke-width="14"
								fill="none"
								stroke-linecap="round"
								:style="{
									strokeDasharray: circumference,
									strokeDashoffset: dashOffset,
									animation: 'draw-ring 1.2s ease forwards',
								}"
								transform="rotate(-90 85 85)"
							/>
						</svg>
						<div class="score-value">{{ result.seo_score }}%</div>
					</div>

					<p style="margin-top: 14px; color: var(--text); font-size: 14px">
						{{ result.url }}
					</p>
				</div>

				<!-- BASIC METRICS -->
				<div class="grid grid-2" style="margin-bottom: 30px">
					<div class="card"><strong>Title:</strong> {{ result.title }}</div>
					<div class="card">
						<strong>Description:</strong> {{ result.meta_description }}
					</div>
					<div class="card"><strong>H1:</strong> {{ result.h1 }}</div>
					<div class="card">
						<strong>Word Count:</strong> {{ result.word_count }}
					</div>
					<div class="card">
						<strong>Internal Links:</strong> {{ result.internal_links }}
					</div>
					<div class="card">
						<strong>External Links:</strong> {{ result.external_links }}
					</div>
					<div class="card">
						<strong>Missing ALTs:</strong>
						<span :class="result.missing_image_alts > 0 ? 'bad' : 'good'">
							{{ result.missing_image_alts }}
						</span>
					</div>
					<div class="card">
						<strong>Viewport Meta:</strong> {{ result.has_viewport_tag }}
					</div>
					<div class="card">
						<strong>Robots.txt:</strong> {{ result.robots_txt_found }}
					</div>
					<div class="card">
						<strong>Sitemap:</strong> {{ result.sitemap_found }}
					</div>
				</div>

				<!-- KEYWORDS -->
				<div class="card" v-if="result.keywords">
					<h2 style="font-size: 22px; margin-bottom: 18px">Top Keywords</h2>

					<div style="display: flex; flex-wrap: wrap; gap: 12px">
						<span
							class="tag"
							v-for="item in result.keywords"
							:key="item.keyword"
						>
							{{ item.keyword }} ({{ item.count }})
						</span>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';

const BACKEND = 'https://seo-audit-tool-production-a57e.up.railway.app';

const url = ref('');
const result = ref(null);
const error = ref('');
const loading = ref(false);

/* DARK MODE */
const darkMode = ref(false);

onMounted(() => {
	const saved = localStorage.getItem('darkMode');
	if (saved === 'true') {
		darkMode.value = true;
		document.documentElement.classList.add('dark');
	}
});

function toggleDark() {
	darkMode.value = !darkMode.value;

	if (darkMode.value) {
		document.documentElement.classList.add('dark');
	} else {
		document.documentElement.classList.remove('dark');
	}

	localStorage.setItem('darkMode', darkMode.value);
}

/* SCORE CIRCLE */
const circumference = 2 * Math.PI * 70;

const dashOffset = computed(() =>
	result.value
		? circumference - (result.value.seo_score / 100) * circumference
		: circumference,
);

const scoreColor = computed(() => {
	if (!result.value) return 'var(--primary)';
	const s = result.value.seo_score;
	if (s >= 80) return 'var(--good)';
	if (s >= 50) return '#f59e0b';
	return 'var(--bad)';
});

/* RUN AUDIT */
async function runAudit() {
	error.value = '';
	result.value = null;

	if (!url.value) {
		error.value = 'Please enter a URL';
		return;
	}

	loading.value = true;

	try {
		const data = await $fetch(`${BACKEND}/seo-audit`, {
			params: { url: url.value },
		});

		if (data.error) error.value = data.error;
		else result.value = data;
	} catch (err) {
		error.value = 'Unable to reach backend.';
	}

	loading.value = false;
}
</script>
