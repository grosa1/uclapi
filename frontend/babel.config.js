'use strict'

module.exports = function(api) {
  api.cache(true)

  return {
    presets: [
      [
        `@babel/preset-env`,
        {
          targets: `> 0.25%, not dead`,
        },
      ],
      `@babel/preset-react`,
    ],
    plugins: [
      `@babel/plugin-syntax-dynamic-import`,
      `@babel/plugin-proposal-class-properties`,
      [
        `transform-imports`,
        {
          lodash: {
            transform: `lodash/\${member}`,
            preventFullImport: true,
          },
        },
      ],
      `@babel/transform-runtime`,
    ],
    env: {
      production: {
        plugins: [
          [
            `transform-react-remove-prop-types`,
            {
              mode: `remove`,
            },
          ],
        ],
      },
    },
  }
}