<template>
	<div class="container">
		<h1
			style="
				font-size: 32px;
				font-weight: bold;
				text-align: center;
				margin-bottom: 12px;
			"
		>
			SEO Audit Tool
		</h1>

		<p style="text-align: center; color: #555; margin-bottom: 32px">
			Enter a URL to analyze its SEO, structure, and performance.
		</p>

		<!-- INPUT -->
		<div style="display: flex; gap: 12px; margin-bottom: 24px">
			<input
				v-model="url"
				type="text"
				class="input"
				placeholder="https://example.com"
			/>
			<button class="btn" @click="runAudit">
				{{ loading ? 'Scanning...' : 'Analyze' }}
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
				<h2 style="font-size: 22px; margin-bottom: 12px">SEO Score</h2>
				<div style="font-size: 40px; font-weight: bold">
					{{ result.seo_score }}%
				</div>
				<p style="margin-top: 10px; color: #555">{{ result.url }}</p>
			</div>

			<!-- BASIC METRICS -->
			<div class="grid grid-2" style="margin-bottom: 24px">
				<div class="card"><strong>Title:</strong> {{ result.title }}</div>
				<div class="card">
					<strong>Meta Description:</strong> {{ result.meta_description }}
				</div>
				<div class="card"><strong>H1 Tag:</strong> {{ result.h1 }}</div>
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
					<strong>Missing Image Alts:</strong>
					<span :class="result.missing_image_alts > 0 ? 'bad' : 'good'">
						{{ result.missing_image_alts }}
					</span>
				</div>

				<div class="card">
					<strong>Viewport Tag:</strong> {{ result.has_viewport_tag }}
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
				<h2 style="font-size: 20px; margin-bottom: 12px">Top Keywords</h2>

				<div style="display: flex; flex-wrap: wrap; gap: 10px">
					<span
						v-for="item in result.keywords"
						:key="item.keyword"
						style="background: #dbeafe; padding: 6px 12px; border-radius: 20px"
					>
						{{ item.keyword }} ({{ item.count }})
					</span>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref } from 'vue';

const BACKEND = 'https://seo-audit-tool-production-a57e.up.railway.app';

const url = ref('');
const result = ref(null);
const error = ref('');
const loading = ref(false);

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
	} catch {
		error.value = 'Could not reach backend.';
	}

	loading.value = false;
}
</script>
