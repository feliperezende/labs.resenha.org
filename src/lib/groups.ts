export type GroupKey = 'systems-wasm' | 'mobile-platform' | 'web-infra' | 'games' | 'foundational';

export const GROUP_LABEL: Record<GroupKey, string> = {
  'systems-wasm': 'systems',
  'mobile-platform': 'mobile',
  'web-infra': 'web',
  'games': 'games',
  'foundational': 'base',
};

export const GROUP_ORDER: GroupKey[] = ['systems-wasm', 'mobile-platform', 'web-infra', 'games', 'foundational'];

export const groupLabel = (g: string) => GROUP_LABEL[g as GroupKey] ?? g;