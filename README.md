# Piney Data Website

This repository contains the source code for the Piney Data website, built using Pelican static site generator.

## Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/pineydata/pineydata.github.io.git
   cd pineydata.github.io
   ```

2. **Set up Python environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run development server**
   ```bash
   python serve.py
   ```
   The site will be available at `http://localhost:5500`

## Development Workflow

### Branch Strategy
1. **Create a feature branch**
   ```bash
   git checkout -b feature/descriptive-name
   ```
   Use prefixes to categorize your changes:
   - `feature/` for new features or content
   - `fix/` for bug fixes
   - `update/` for content updates
   - `design/` for theme changes

2. **Make your changes**
   - Keep commits focused and atomic
   - Write clear commit messages
   - Test changes locally using `serve.py`

3. **Create a Pull Request**
   - Push your branch to GitHub:
     ```bash
     git push origin feature/descriptive-name
     ```
   - Go to GitHub and create a PR
   - Fill out the PR template with:
     - Description of changes
     - Screenshots (if visual changes)
     - Any related issues
     - Testing steps

4. **PR Review Process**
   - Request review from team members
   - Address any feedback
   - Make sure GitHub Actions checks pass
   - Squash and merge when approved

5. **After Merge**
   - GitHub Actions will automatically deploy
   - Verify changes on the live site
   - Delete the feature branch

## Making Changes

### Content Structure
- `content/pages/`: Markdown files for static pages
- `themes/piney/`: Custom theme files
  - `static/`: CSS, JavaScript, and other static assets
  - `templates/`: Jinja2 HTML templates

### Configuration Files
- `pelicanconf.py`: Development settings
- `publishconf.py`: Production settings
- `.github/workflows/deploy.yml`: Deployment automation

## Deployment

The site is automatically deployed using GitHub Actions whenever changes are merged to the `main` branch through a PR.

1. **Automatic Deployment**
   - GitHub Actions will automatically:
     - Build the site using `publishconf.py`
     - Deploy to GitHub Pages
     - Preserve CNAME for custom domain

2. **Verify Deployment**
   - Check the Actions tab in GitHub for build status
   - Visit [www.pineydata.com](https://www.pineydata.com) to see your changes

## Custom Domain Setup

The site uses a custom domain (www.pineydata.com) configured through:
- `content/extra/CNAME` file
- GitHub Pages settings

## Theme Development

The custom theme uses:
- Tailwind CSS for styling
- Bootstrap Icons for icons
- Custom geometric patterns and animations

Brand Colors:
- Primary: `#009477`
- Secondary: `#2fa1ba`


## Troubleshooting

If the site isn't updating:
1. Check GitHub Actions for any build errors
2. Verify PR was properly merged to `main` branch
3. Check that CNAME file is present in the deployed site

## Need Help?

Contact [hello@pineydata.com](mailto:hello@pineydata.com) for support.
