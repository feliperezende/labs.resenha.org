import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';
import { siteTitle, siteDescription, siteUrl } from '../config/site';

const esc = (s: string) =>
  s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

export const GET: APIRoute = async () => {
  const experiments = await getCollection('experiments');
  const items = experiments
    .filter((e) => e.data.status !== 'archived')
    .sort((a, b) => +new Date(b.data.updatedAt) - +new Date(a.data.updatedAt))
    .map((e) => {
      const slug = e.data.slug ?? e.id;
      const url = `${siteUrl}/experiments/${slug}`;
      return `    <item>
      <title>${esc(e.data.title)}</title>
      <link>${url}</link>
      <guid isPermaLink="true">${url}</guid>
      <pubDate>${new Date(e.data.updatedAt).toUTCString()}</pubDate>
      <description>${esc(e.data.description)}</description>
    </item>`;
    })
    .join('\n');

  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>${esc(siteTitle)}</title>
    <link>${siteUrl}</link>
    <description>${esc(siteDescription)}</description>
    <language>pt-BR</language>
    <lastBuildDate>${new Date().toUTCString()}</lastBuildDate>
${items}
  </channel>
</rss>
`;

  return new Response(xml, { headers: { 'Content-Type': 'application/xml; charset=utf-8' } });
};