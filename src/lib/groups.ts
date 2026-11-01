export type GroupKey = 'systems-wasm' | 'mobile-platform' | 'web-infra' | 'foundational';

export const GROUP_LABEL: Record<GroupKey, string> = {
  'systems-wasm': 'systems',
  'mobile-platform': 'mobile',
  'web-infra': 'web',
  'foundational': 'base',
};

export const GROUP_ORDER: GroupKey[] = ['systems-wasm', 'mobile-platform', 'web-infra', 'foundational'];

export const groupLabel = (g: string) => GROUP_LABEL[g as GroupKey] ?? g;