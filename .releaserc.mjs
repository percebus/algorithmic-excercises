/**
 * @type {import('semantic-release').GlobalConfig}
 */
export default {
  branches: ["main", "next"],
  plugins: [
    "@semantic-release/commit-analyzer",
    "@semantic-release/release-notes-generator",
    [
      "@semantic-release/changelog",
      {
        changelogFile: "CHANGELOG.md",
      },
    ],
    [
      "@semantic-release/npm",
      {
        npmPublish: false,
        tarballDir: "dist",
      },
    ],
    [
      "@semantic-release/github",
      {
        assets: [
          {path: "CHANGELOG"}, // XXX?
          {path: "dist/*.tgz"}
        ],
      },
    ],
    [
      "@semantic-release/git",
      {
        assets: ["package.json"],
        changelogFile: "CHANGELOG.md",
      },
    ],
  ],
};
