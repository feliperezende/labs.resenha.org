import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const experiments = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/experiments' }),
  schema: z.object({
    title: z.string(),
    slug: z.string(),
    group: z.enum(['systems-wasm', 'mobile-platform', 'web-infra', 'foundational']),
    language: z.string(),
    description: z.string(),
    updatedAt: z.coerce.date(),
    stars: z.number().default(0),
    status: z.enum(['active', 'archived', 'learning']).default('active'),
    private: z.boolean().default(false),
    github: z.string().url().optional(),
    demo: z.string().url().optional(),
    tags: z.array(z.string()).default([]),
  }),
});

const labReports = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/lab-reports' }),
  schema: z.object({
    title: z.string(),
    slug: z.string(),
    date: z.string().date(),
    description: z.string(),
    readTime: z.string(),
    tags: z.array(z.string()).default([]),
  }),
});

export const collections = { experiments, labReports };