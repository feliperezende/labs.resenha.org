// Site metadata. URLs are base-aware so the same build works on project pages
// (feliperezende.github.io/labs.resenha.org) and on the custom domain.
const base = import.meta.env.BASE_URL.replace(/\/$/, ''); // '' | '/labs.resenha.org'

export const withBase = (path: string) => `${base}/${path.replace(/^\//, '')}`;

export const siteUrl = `${import.meta.env.SITE.replace(/\/$/, '')}${base}`;

export const siteTitle = 'labs.resenha.org';
export const siteDescription =
  'Technical experiments across systems, mobile, and web. A living lab notebook by Felipe Rezende.';
export const author = 'Felipe Rezende';
export const authorTitle = 'Engineering Manager @ Nubank';
export const authorLocation = 'São Paulo, BR';
export const githubUrl = 'https://github.com/feliperezende';
export const linkedinUrl = 'https://linkedin.com/in/felipe-rezende-em';
export const rssUrl = withBase('/rss.xml');
export const sourceUrl = 'https://github.com/feliperezende/labs.resenha.org';