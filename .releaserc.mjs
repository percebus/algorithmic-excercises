/**
 * @type {import('semantic-release').GlobalConfig}
 */
export default {
  branches: ["main", "next"],
  exec: {
    generateNotes: ["npm run style"],
  },
  plugins: [
    "@semantic-release/commit-analyzer",
    "@semantic-release/release-notes-generator",
    [
      "@semantic-release/changelog",
      {
        changelogTitle: "# algorithmic-excercises CHANGELOG",
      },
    ],
    [
      "@semantic-release/npm",
      {
        npmPublish: false,
        tarballDir: "dist",
      },
    ],
    "@semantic-release/exec",
    [
      "@semantic-release/git",
      {
        assets: [
          "package.json",
          "CHANGELOG.md",
          "requirements.all.txt",
          "requirements.main.txt",
        ],
        changelogFile: "CHANGELOG.md",
      },
    ],
    [
      "@semantic-release/github",
      {
        assets: [{ path: "dist/*.tgz" }],
      },
    ],
  ],
};
