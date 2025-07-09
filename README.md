# Mastering Industrial Image Processing

A comprehensive Hugo-based website for learning industrial computer vision and image processing with MIL, OpenCV, and practical tutorials.

## 🚀 Quick Start

### Prerequisites

- [Hugo Extended](https://gohugo.io/installation/) (v0.121.0 or later)
- [Git](https://git-scm.com/)
- [Node.js](https://nodejs.org/) (optional, for npm scripts)

### Local Development

1. **Clone the repository**
   ```bash
   git clone --recursive https://github.com/brmel/ibraverse_web.git
   cd ibraverse_web
   ```

2. **Start development server**
   ```bash
   ./scripts/start-dev.sh
   # or
   hugo server -D
   ```

3. **Open your browser**
   Navigate to `http://localhost:1313`

## 📝 Content Management

### Creating New Posts

Use the automated script to create new blog posts:

```bash
./scripts/new-post.sh "Your Post Title"
```

This will:
- Create a new post directory in `content/posts/`
- Generate a post file with proper front matter
- Create an `images/` folder for post assets
- Set the post as draft by default

### Manual Post Creation

```bash
hugo new posts/your-post-title/index.md
```

### Adding Images

1. Place images in `content/posts/your-post/images/`
2. Reference them in your markdown: `![Description](images/your-image.jpg)`
3. Optimize images using: `./scripts/optimize-images.sh content/posts/your-post/images/`

## 🛠️ Build and Deployment

### Local Build

```bash
./scripts/build.sh
# or
hugo --gc --minify
```

### GitHub Pages Deployment

This site automatically deploys to GitHub Pages via GitHub Actions when you push to the `main` branch.

### Netlify Deployment

The site is configured for Netlify deployment with the included `netlify.toml` file.

## 🎨 Customization

### Theme Configuration

The site uses the PaperMod theme. Key configurations are in `config.toml`:

- **Site Information**: Update title, description, and author details
- **Social Links**: Configure your social media profiles
- **Analytics**: Add your Google Analytics tracking ID
- **Newsletter**: Configure Buttondown integration

### Custom Styling

Add custom CSS in `assets/css/extended/custom.css`

### Custom Layouts

Override theme layouts by creating files in the `layouts/` directory

## 📊 Analytics and SEO

### Google Analytics 4

1. Create a GA4 property
2. Update `config.toml` with your Measurement ID:
   ```toml
   [params.analytics]
   google = "G-XXXXXXXXXX"
   ```

### Search Console

1. Verify ownership in Google Search Console
2. Update the verification tag in `config.toml`

### SEO Optimization

- Customize meta descriptions for each post
- Use descriptive alt text for images
- Optimize post URLs and titles
- Submit sitemap to search engines

## 🔧 Available Scripts

| Script | Description |
|--------|-------------|
| `./scripts/start-dev.sh` | Start development server |
| `./scripts/build.sh` | Build for production |
| `./scripts/new-post.sh "Title"` | Create new blog post |
| `./scripts/optimize-images.sh path/` | Optimize images |
| `./scripts/update-theme.sh` | Update PaperMod theme |
| `./scripts/backup.sh` | Backup content and config |

### NPM Scripts

```bash
npm run dev          # Start development server
npm run build        # Build for production
npm run new-post     # Create new post (requires title argument)
```

## 📁 Project Structure

```
ibraverse_web/
├── .github/workflows/       # GitHub Actions
├── content/                 # Site content
│   ├── posts/              # Blog posts
│   ├── about.md            # About page
│   ├── contact.md          # Contact page
│   └── _index.md           # Homepage
├── static/                 # Static assets
├── layouts/                # Custom layouts
├── assets/                 # Theme assets
├── scripts/                # Automation scripts
├── config.toml            # Site configuration
├── netlify.toml           # Netlify configuration
└── package.json           # NPM configuration
```

## 🔄 Content Workflow

1. **Create new post**: `./scripts/new-post.sh "Post Title"`
2. **Add content**: Edit the generated markdown file
3. **Add images**: Place in the post's `images/` folder
4. **Optimize images**: `./scripts/optimize-images.sh content/posts/post-name/images/`
5. **Preview**: `hugo server -D`
6. **Publish**: Remove `draft: true` from front matter
7. **Deploy**: Commit and push to trigger automatic deployment

## 🌐 Deployment Options

### GitHub Pages (Current Setup)
- Automatic deployment via GitHub Actions
- Free hosting for public repositories
- Custom domain support

### Netlify
- Configured via `netlify.toml`
- Automatic deployments from Git
- Free tier available with custom domains

### Other Platforms
- Vercel: Deploy the `public/` folder
- AWS S3: Static website hosting
- Self-hosted: Deploy built files to any web server

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally
5. Submit a pull request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Documentation**: [Hugo Documentation](https://gohugo.io/documentation/)
- **Theme**: [PaperMod Documentation](https://github.com/adityatelange/hugo-PaperMod)
- **Issues**: [Report bugs or request features](https://github.com/brmel/ibraverse_web/issues)

## 🎯 Roadmap

- [ ] Add interactive code examples
- [ ] Implement comment system
- [ ] Add search functionality
- [ ] Create video tutorial integration
- [ ] Add downloadable resources section

---

Made with ❤️ for the industrial image processing community
