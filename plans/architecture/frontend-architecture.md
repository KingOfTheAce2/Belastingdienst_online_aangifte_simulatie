# Frontend Architecture Plan: Dutch Tax Forms Web Application

## Executive Summary

This document outlines the comprehensive frontend architecture for modernizing the Dutch tax forms system from a Google Web Toolkit (GWT) based application to a modern, scalable web application using ViteJS, ShadCN UI, and responsive design principles.

## Architecture Overview

### Technology Stack

- **Build Tool**: ViteJS 5.x
- **Framework**: React 18.x with TypeScript
- **UI Library**: ShadCN UI (Radix UI + Tailwind CSS)
- **State Management**: Zustand + React Query
- **Styling**: Tailwind CSS with CSS Modules
- **Forms**: React Hook Form + Zod validation
- **Testing**: Vitest + React Testing Library + Playwright
- **Deployment**: Containerized with Docker

### Core Principles

1. **Progressive Enhancement**: Mobile-first, accessibility-first approach
2. **Modular Design**: Composable components and services
3. **Type Safety**: Full TypeScript implementation
4. **Performance**: Code splitting, lazy loading, and caching
5. **Security**: Client-side encryption, secure form handling
6. **Maintainability**: Clean code, comprehensive testing
7. **Scalability**: Microservices-ready architecture

## 1. Project Structure

### Root Directory Organization

```
dutch-tax-frontend/
├── .env.example                 # Environment variables template
├── .env.local                   # Local development environment
├── .gitignore                   # Git ignore patterns
├── Dockerfile                   # Container configuration
├── README.md                    # Project documentation
├── docker-compose.yml           # Local development setup
├── index.html                   # Main HTML template
├── package.json                 # Dependencies and scripts
├── tailwind.config.js           # Tailwind CSS configuration
├── tsconfig.json                # TypeScript configuration
├── vite.config.ts               # Vite build configuration
├── vitest.config.ts             # Test configuration
├── playwright.config.ts         # E2E test configuration
│
├── public/                      # Static assets
│   ├── favicon.ico
│   ├── manifest.json
│   ├── robots.txt
│   └── icons/
│       ├── icon-192x192.png
│       └── icon-512x512.png
│
├── src/                         # Application source code
│   ├── main.tsx                 # Application entry point
│   ├── App.tsx                  # Root component
│   ├── index.css                # Global styles
│   │
│   ├── components/              # Reusable UI components
│   │   ├── ui/                  # ShadCN base components
│   │   ├── forms/               # Form-specific components
│   │   ├── layout/              # Layout components
│   │   ├── navigation/          # Navigation components
│   │   └── common/              # Common utility components
│   │
│   ├── pages/                   # Page components
│   │   ├── auth/                # Authentication pages
│   │   ├── dashboard/           # User dashboard
│   │   ├── forms/               # Tax form pages
│   │   ├── help/                # Help and support
│   │   └── settings/            # User settings
│   │
│   ├── features/                # Feature-based modules
│   │   ├── corporate-tax/       # Corporate tax form (CA)
│   │   ├── income-tax/          # Income tax form (IB)
│   │   ├── monthly-declaration/ # Monthly declaration (MA)
│   │   ├── payroll-admin/       # Payroll administration (PA)
│   │   └── vat-declaration/     # VAT declaration (VA)
│   │
│   ├── services/                # API and business logic
│   │   ├── api/                 # API service layers
│   │   ├── auth/                # Authentication services
│   │   ├── calculations/        # Tax calculation engine
│   │   ├── validation/          # Form validation services
│   │   └── storage/             # Local storage services
│   │
│   ├── hooks/                   # Custom React hooks
│   │   ├── useAuth.ts           # Authentication hook
│   │   ├── useForm.ts           # Form management hook
│   │   ├── useLocalStorage.ts   # Local storage hook
│   │   └── useTaxCalculation.ts # Tax calculation hook
│   │
│   ├── stores/                  # State management
│   │   ├── authStore.ts         # Authentication state
│   │   ├── formStore.ts         # Form state management
│   │   ├── settingsStore.ts     # User settings state
│   │   └── calculationStore.ts  # Tax calculation state
│   │
│   ├── utils/                   # Utility functions
│   │   ├── formatters.ts        # Data formatting utilities
│   │   ├── validators.ts        # Validation utilities
│   │   ├── constants.ts         # Application constants
│   │   ├── helpers.ts           # General helper functions
│   │   └── types.ts             # TypeScript type definitions
│   │
│   ├── assets/                  # Static assets
│   │   ├── images/              # Images and icons
│   │   ├── fonts/               # Custom fonts
│   │   └── styles/              # Additional stylesheets
│   │
│   └── locales/                 # Internationalization
│       ├── nl/                  # Dutch translations
│       ├── en/                  # English translations
│       └── index.ts             # i18n configuration
│
├── tests/                       # Test files
│   ├── __mocks__/               # Mock implementations
│   ├── e2e/                     # End-to-end tests
│   ├── integration/             # Integration tests
│   ├── unit/                    # Unit tests
│   └── setup.ts                 # Test setup configuration
│
├── docs/                        # Documentation
│   ├── architecture/            # Architecture documentation
│   ├── api/                     # API documentation
│   ├── deployment/              # Deployment guides
│   └── user-guide/              # User documentation
│
└── scripts/                     # Build and deployment scripts
    ├── build.sh                 # Production build script
    ├── deploy.sh                # Deployment script
    └── test.sh                  # Test execution script
```

### Component Hierarchy

```
App
├── AuthProvider
├── ThemeProvider
├── ErrorBoundary
├── Router
│   ├── PublicRoutes
│   │   ├── LoginPage
│   │   ├── RegisterPage
│   │   └── ForgotPasswordPage
│   │
│   └── PrivateRoutes
│       ├── DashboardLayout
│       │   ├── Header
│       │   ├── Sidebar
│       │   ├── MainContent
│       │   └── Footer
│       │
│       ├── Dashboard
│       ├── TaxFormRouter
│       │   ├── CorporateTaxForm
│       │   ├── IncomeTaxForm
│       │   ├── MonthlyDeclarationForm
│       │   ├── PayrollAdminForm
│       │   └── VATDeclarationForm
│       │
│       ├── HelpCenter
│       └── UserSettings
```

## 2. ViteJS Integration

### Build Configuration

```typescript
// vite.config.ts
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { resolve } from 'path'

export default defineConfig({
  plugins: [react()],
  
  // Development server configuration
  server: {
    port: 3000,
    host: true,
    hmr: {
      overlay: true
    }
  },
  
  // Build configuration
  build: {
    target: 'esnext',
    outDir: 'dist',
    assetsDir: 'assets',
    sourcemap: true,
    minify: 'terser',
    
    // Code splitting configuration
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
      },
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'],
          ui: ['@radix-ui/react-dialog', '@radix-ui/react-form'],
          utils: ['date-fns', 'lodash-es']
        }
      }
    },
    
    // Chunk size warnings
    chunkSizeWarningLimit: 1000
  },
  
  // Path resolution
  resolve: {
    alias: {
      '@': resolve(__dirname, 'src'),
      '@components': resolve(__dirname, 'src/components'),
      '@pages': resolve(__dirname, 'src/pages'),
      '@features': resolve(__dirname, 'src/features'),
      '@services': resolve(__dirname, 'src/services'),
      '@hooks': resolve(__dirname, 'src/hooks'),
      '@stores': resolve(__dirname, 'src/stores'),
      '@utils': resolve(__dirname, 'src/utils'),
      '@assets': resolve(__dirname, 'src/assets'),
      '@locales': resolve(__dirname, 'src/locales')
    }
  },
  
  // Environment variables
  define: {
    __DEV__: JSON.stringify(process.env.NODE_ENV === 'development'),
    __PROD__: JSON.stringify(process.env.NODE_ENV === 'production'),
    __VERSION__: JSON.stringify(process.env.npm_package_version)
  },
  
  // CSS configuration
  css: {
    modules: {
      localsConvention: 'camelCaseOnly'
    },
    preprocessorOptions: {
      scss: {
        additionalData: `@import "@/assets/styles/variables.scss";`
      }
    }
  }
})
```

### Development Setup

```json
// package.json scripts
{
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "preview": "vite preview",
    "test": "vitest",
    "test:e2e": "playwright test",
    "test:coverage": "vitest run --coverage",
    "lint": "eslint . --ext ts,tsx --report-unused-disable-directives --max-warnings 0",
    "lint:fix": "eslint . --ext ts,tsx --fix",
    "type-check": "tsc --noEmit",
    "format": "prettier --write .",
    "analyze": "npm run build && npx vite-bundle-analyzer dist/stats.html"
  }
}
```

### Hot Module Replacement (HMR)

```typescript
// src/main.tsx
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App'

const container = document.getElementById('root')
const root = createRoot(container!)

root.render(
  <StrictMode>
    <App />
  </StrictMode>
)

// Enable HMR
if (import.meta.hot) {
  import.meta.hot.accept()
}
```

### Production Optimization

```typescript
// Production build optimizations
export default defineConfig({
  build: {
    // Minification
    minify: 'terser',
    terserOptions: {
      compress: {
        drop_console: true,
        drop_debugger: true
      }
    },
    
    // Asset optimization
    assetsInlineLimit: 4096,
    
    // CSS optimization
    cssMinify: true,
    
    // Bundle analysis
    reportCompressedSize: true,
    
    // Legacy support
    target: ['es2015', 'chrome58', 'firefox57', 'safari11']
  }
})
```

## 3. ShadCN UI Integration

### Component Library Setup

```bash
# Initialize ShadCN UI
npx shadcn-ui@latest init
```

```typescript
// components.json
{
  "style": "default",
  "rsc": false,
  "tsx": true,
  "tailwind": {
    "config": "tailwind.config.js",
    "css": "src/index.css",
    "baseColor": "slate",
    "cssVariables": true
  },
  "aliases": {
    "components": "@/components",
    "utils": "@/utils"
  }
}
```

### Theme Configuration

```typescript
// src/components/theme-provider.tsx
import { createContext, useContext, useEffect, useState } from 'react'

type Theme = 'dark' | 'light' | 'system'

type ThemeProviderProps = {
  children: React.ReactNode
  defaultTheme?: Theme
  storageKey?: string
}

const ThemeProviderContext = createContext<{
  theme: Theme
  setTheme: (theme: Theme) => void
}>({
  theme: 'system',
  setTheme: () => null,
})

export function ThemeProvider({
  children,
  defaultTheme = 'system',
  storageKey = 'dutch-tax-theme',
}: ThemeProviderProps) {
  const [theme, setTheme] = useState<Theme>(
    () => (localStorage.getItem(storageKey) as Theme) || defaultTheme
  )

  useEffect(() => {
    const root = window.document.documentElement
    root.classList.remove('light', 'dark')

    if (theme === 'system') {
      const systemTheme = window.matchMedia('(prefers-color-scheme: dark)')
        .matches
        ? 'dark'
        : 'light'
      root.classList.add(systemTheme)
    } else {
      root.classList.add(theme)
    }
  }, [theme])

  return (
    <ThemeProviderContext.Provider value={{ theme, setTheme }}>
      {children}
    </ThemeProviderContext.Provider>
  )
}

export const useTheme = () => {
  const context = useContext(ThemeProviderContext)
  if (!context) {
    throw new Error('useTheme must be used within a ThemeProvider')
  }
  return context
}
```

### Custom Component Development

```typescript
// src/components/ui/form-field.tsx
import { cn } from '@/utils/cn'
import { forwardRef } from 'react'

interface FormFieldProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label?: string
  error?: string
  helper?: string
  required?: boolean
}

const FormField = forwardRef<HTMLInputElement, FormFieldProps>(
  ({ className, label, error, helper, required, ...props }, ref) => {
    return (
      <div className="space-y-2">
        {label && (
          <label
            htmlFor={props.id}
            className="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
          >
            {label}
            {required && <span className="text-red-500 ml-1">*</span>}
          </label>
        )}
        <input
          ref={ref}
          className={cn(
            "flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50",
            error && "border-red-500 focus-visible:ring-red-500",
            className
          )}
          {...props}
        />
        {error && (
          <p className="text-sm text-red-500">{error}</p>
        )}
        {helper && !error && (
          <p className="text-sm text-muted-foreground">{helper}</p>
        )}
      </div>
    )
  }
)

FormField.displayName = 'FormField'
export { FormField }
```

### Accessibility Compliance

```typescript
// src/components/ui/accessible-form.tsx
import { useId } from 'react'
import { Label } from '@/components/ui/label'
import { Input } from '@/components/ui/input'
import { cn } from '@/utils/cn'

interface AccessibleFormFieldProps {
  label: string
  error?: string
  helper?: string
  required?: boolean
  children: React.ReactNode
}

export function AccessibleFormField({
  label,
  error,
  helper,
  required,
  children,
}: AccessibleFormFieldProps) {
  const id = useId()
  const helperId = useId()
  const errorId = useId()

  return (
    <div className="space-y-2">
      <Label
        htmlFor={id}
        className={cn(
          "text-sm font-medium",
          required && "after:content-['*'] after:ml-0.5 after:text-red-500"
        )}
      >
        {label}
      </Label>
      
      <div className="relative">
        {React.cloneElement(children as React.ReactElement, {
          id,
          'aria-describedby': [
            helper && helperId,
            error && errorId,
          ].filter(Boolean).join(' '),
          'aria-invalid': error ? 'true' : 'false',
          'aria-required': required ? 'true' : 'false',
        })}
      </div>
      
      {helper && !error && (
        <p
          id={helperId}
          className="text-sm text-muted-foreground"
          role="status"
        >
          {helper}
        </p>
      )}
      
      {error && (
        <p
          id={errorId}
          className="text-sm text-red-500"
          role="alert"
          aria-live="polite"
        >
          {error}
        </p>
      )}
    </div>
  )
}
```

## 4. Responsive Design Strategy

### Mobile-First Approach

```css
/* src/index.css - Mobile-first breakpoints */
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  /* Base styles for mobile */
  * {
    box-sizing: border-box;
  }
  
  html {
    font-size: 16px;
    scroll-behavior: smooth;
  }
  
  body {
    font-family: 'Inter', system-ui, sans-serif;
    line-height: 1.6;
    color: hsl(var(--foreground));
    background: hsl(var(--background));
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }
}

@layer components {
  /* Mobile-first form styles */
  .tax-form {
    @apply w-full max-w-md mx-auto p-4 space-y-4;
  }
  
  .tax-form-section {
    @apply bg-card rounded-lg border p-4 space-y-3;
  }
  
  .tax-form-actions {
    @apply flex flex-col space-y-2 pt-4;
  }
  
  /* Tablet styles */
  @media (min-width: 768px) {
    .tax-form {
      @apply max-w-2xl p-6 space-y-6;
    }
    
    .tax-form-section {
      @apply p-6 space-y-4;
    }
    
    .tax-form-actions {
      @apply flex-row space-y-0 space-x-3 justify-end;
    }
  }
  
  /* Desktop styles */
  @media (min-width: 1024px) {
    .tax-form {
      @apply max-w-4xl p-8 space-y-8;
    }
    
    .tax-form-section {
      @apply p-8 space-y-6;
    }
  }
}
```

### Responsive Grid System

```typescript
// src/components/layout/responsive-grid.tsx
import { cn } from '@/utils/cn'

interface ResponsiveGridProps {
  children: React.ReactNode
  className?: string
  cols?: {
    default: number
    sm?: number
    md?: number
    lg?: number
    xl?: number
  }
  gap?: number
}

export function ResponsiveGrid({
  children,
  className,
  cols = { default: 1, md: 2, lg: 3 },
  gap = 4,
}: ResponsiveGridProps) {
  const gridClasses = cn(
    'grid',
    `grid-cols-${cols.default}`,
    cols.sm && `sm:grid-cols-${cols.sm}`,
    cols.md && `md:grid-cols-${cols.md}`,
    cols.lg && `lg:grid-cols-${cols.lg}`,
    cols.xl && `xl:grid-cols-${cols.xl}`,
    `gap-${gap}`,
    className
  )

  return <div className={gridClasses}>{children}</div>
}
```

### Progressive Enhancement

```typescript
// src/hooks/useResponsive.ts
import { useEffect, useState } from 'react'

type Breakpoint = 'sm' | 'md' | 'lg' | 'xl'

const breakpoints = {
  sm: 640,
  md: 768,
  lg: 1024,
  xl: 1280,
}

export function useResponsive() {
  const [screenSize, setScreenSize] = useState<Breakpoint>('sm')

  useEffect(() => {
    const handleResize = () => {
      const width = window.innerWidth
      
      if (width >= breakpoints.xl) {
        setScreenSize('xl')
      } else if (width >= breakpoints.lg) {
        setScreenSize('lg')
      } else if (width >= breakpoints.md) {
        setScreenSize('md')
      } else {
        setScreenSize('sm')
      }
    }

    handleResize()
    window.addEventListener('resize', handleResize)
    return () => window.removeEventListener('resize', handleResize)
  }, [])

  return {
    screenSize,
    isMobile: screenSize === 'sm',
    isTablet: screenSize === 'md',
    isDesktop: screenSize === 'lg' || screenSize === 'xl',
    isXLDesktop: screenSize === 'xl',
  }
}
```

## 5. Form Architecture

### Tax Form Component Structure

```typescript
// src/features/corporate-tax/components/CorporateTaxForm.tsx
import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { CorporateTaxSchema, CorporateTaxFormData } from './schema'
import { FormSection } from '@/components/forms/FormSection'
import { TaxFormLayout } from '@/components/layout/TaxFormLayout'

export function CorporateTaxForm() {
  const form = useForm<CorporateTaxFormData>({
    resolver: zodResolver(CorporateTaxSchema),
    defaultValues: {
      companyDetails: {
        name: '',
        kvkNumber: '',
        taxNumber: '',
      },
      financialData: {
        revenue: 0,
        expenses: 0,
        profit: 0,
      },
      taxCalculation: {
        corporateTaxRate: 0.25,
        taxableProfit: 0,
        taxOwed: 0,
      },
    },
  })

  return (
    <TaxFormLayout
      title="Corporate Tax Declaration (CA-2024)"
      description="Complete your corporate tax return for fiscal year 2024"
    >
      <Form {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
          <FormSection
            title="Company Details"
            description="Enter your company registration information"
          >
            <CompanyDetailsFields />
          </FormSection>

          <FormSection
            title="Financial Information"
            description="Provide your annual financial figures"
          >
            <FinancialDataFields />
          </FormSection>

          <FormSection
            title="Tax Calculation"
            description="Review calculated tax amounts"
          >
            <TaxCalculationFields />
          </FormSection>

          <FormActions />
        </form>
      </Form>
    </TaxFormLayout>
  )
}
```

### Validation Framework

```typescript
// src/features/corporate-tax/schema.ts
import { z } from 'zod'

export const CorporateTaxSchema = z.object({
  companyDetails: z.object({
    name: z.string().min(1, 'Company name is required'),
    kvkNumber: z.string().regex(/^\d{8}$/, 'KvK number must be 8 digits'),
    taxNumber: z.string().regex(/^\d{9}B\d{2}$/, 'Invalid tax number format'),
  }),
  
  financialData: z.object({
    revenue: z.number().min(0, 'Revenue cannot be negative'),
    expenses: z.number().min(0, 'Expenses cannot be negative'),
    profit: z.number(),
  }).refine(
    (data) => data.profit === data.revenue - data.expenses,
    {
      message: 'Profit must equal revenue minus expenses',
      path: ['profit'],
    }
  ),
  
  taxCalculation: z.object({
    corporateTaxRate: z.number().min(0).max(1),
    taxableProfit: z.number().min(0),
    taxOwed: z.number().min(0),
  }),
})

export type CorporateTaxFormData = z.infer<typeof CorporateTaxSchema>
```

### State Management

```typescript
// src/stores/formStore.ts
import { create } from 'zustand'
import { persist } from 'zustand/middleware'

interface FormState {
  forms: Record<string, any>
  currentForm: string | null
  isDirty: boolean
  lastSaved: Date | null
  
  // Actions
  setForm: (formId: string, data: any) => void
  updateForm: (formId: string, updates: Partial<any>) => void
  clearForm: (formId: string) => void
  setCurrentForm: (formId: string) => void
  markDirty: () => void
  markClean: () => void
}

export const useFormStore = create<FormState>()(
  persist(
    (set, get) => ({
      forms: {},
      currentForm: null,
      isDirty: false,
      lastSaved: null,
      
      setForm: (formId, data) => {
        set((state) => ({
          forms: { ...state.forms, [formId]: data },
          isDirty: true,
        }))
      },
      
      updateForm: (formId, updates) => {
        set((state) => ({
          forms: {
            ...state.forms,
            [formId]: { ...state.forms[formId], ...updates },
          },
          isDirty: true,
        }))
      },
      
      clearForm: (formId) => {
        set((state) => {
          const { [formId]: _, ...rest } = state.forms
          return { forms: rest }
        })
      },
      
      setCurrentForm: (formId) => {
        set({ currentForm: formId })
      },
      
      markDirty: () => set({ isDirty: true }),
      markClean: () => set({ isDirty: false, lastSaved: new Date() }),
    }),
    {
      name: 'dutch-tax-forms',
      partialize: (state) => ({ forms: state.forms }),
    }
  )
)
```

### Data Flow Patterns

```typescript
// src/hooks/useTaxForm.ts
import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { useFormStore } from '@/stores/formStore'
import { useTaxCalculation } from '@/hooks/useTaxCalculation'
import { useAutoSave } from '@/hooks/useAutoSave'

export function useTaxForm<T>(
  formId: string,
  schema: any,
  defaultValues: T
) {
  const { forms, setForm, updateForm } = useFormStore()
  const { calculateTax } = useTaxCalculation()
  
  const form = useForm<T>({
    resolver: zodResolver(schema),
    defaultValues: forms[formId] || defaultValues,
  })

  const { watch, setValue, handleSubmit } = form

  // Auto-save functionality
  useAutoSave(formId, watch(), 30000) // Save every 30 seconds

  // Auto-calculate when financial data changes
  useEffect(() => {
    const subscription = watch((value, { name }) => {
      if (name?.includes('financial')) {
        const taxData = calculateTax(value)
        setValue('taxCalculation', taxData)
      }
    })
    return () => subscription.unsubscribe()
  }, [watch, setValue, calculateTax])

  const onSubmit = handleSubmit(async (data) => {
    try {
      await submitTaxForm(formId, data)
      setForm(formId, data)
    } catch (error) {
      console.error('Form submission error:', error)
    }
  })

  return {
    form,
    onSubmit,
    isDirty: form.formState.isDirty,
    isValid: form.formState.isValid,
  }
}
```

## 6. Performance Optimization

### Code Splitting

```typescript
// src/utils/lazy-imports.ts
import { lazy } from 'react'

// Lazy load tax form components
export const CorporateTaxForm = lazy(
  () => import('@/features/corporate-tax/components/CorporateTaxForm')
)

export const IncomeTaxForm = lazy(
  () => import('@/features/income-tax/components/IncomeTaxForm')
)

export const VATDeclarationForm = lazy(
  () => import('@/features/vat-declaration/components/VATDeclarationForm')
)

// Route-based code splitting
export const Dashboard = lazy(() => import('@/pages/dashboard/Dashboard'))
export const HelpCenter = lazy(() => import('@/pages/help/HelpCenter'))
export const UserSettings = lazy(() => import('@/pages/settings/UserSettings'))
```

### Lazy Loading Implementation

```typescript
// src/components/common/LazyComponent.tsx
import { Suspense } from 'react'
import { Skeleton } from '@/components/ui/skeleton'

interface LazyComponentProps {
  children: React.ReactNode
  fallback?: React.ReactNode
}

export function LazyComponent({ children, fallback }: LazyComponentProps) {
  const defaultFallback = (
    <div className="space-y-4">
      <Skeleton className="h-8 w-full" />
      <Skeleton className="h-64 w-full" />
      <Skeleton className="h-8 w-32" />
    </div>
  )

  return (
    <Suspense fallback={fallback || defaultFallback}>
      {children}
    </Suspense>
  )
}
```

### Bundle Optimization

```typescript
// vite.config.ts - Advanced optimization
export default defineConfig({
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          // Vendor chunks
          'react-vendor': ['react', 'react-dom', 'react-router-dom'],
          'ui-vendor': ['@radix-ui/react-dialog', '@radix-ui/react-form'],
          'form-vendor': ['react-hook-form', 'zod', '@hookform/resolvers'],
          'util-vendor': ['date-fns', 'lodash-es'],
          
          // Feature chunks
          'corporate-tax': ['@/features/corporate-tax'],
          'income-tax': ['@/features/income-tax'],
          'vat-declaration': ['@/features/vat-declaration'],
        },
      },
    },
  },
  
  // Asset optimization
  assetsInclude: ['**/*.woff2', '**/*.woff'],
  
  // Preload critical resources
  optimizeDeps: {
    include: ['react', 'react-dom', 'react-router-dom'],
    exclude: ['@/features/**'],
  },
})
```

### Caching Strategies

```typescript
// src/services/cache.ts
class CacheService {
  private cache = new Map<string, { data: any; timestamp: number; ttl: number }>()

  set(key: string, data: any, ttl: number = 300000) { // 5 minutes default
    this.cache.set(key, {
      data,
      timestamp: Date.now(),
      ttl,
    })
  }

  get(key: string) {
    const entry = this.cache.get(key)
    if (!entry) return null

    const isExpired = Date.now() - entry.timestamp > entry.ttl
    if (isExpired) {
      this.cache.delete(key)
      return null
    }

    return entry.data
  }

  clear() {
    this.cache.clear()
  }
}

export const cacheService = new CacheService()

// Service Worker for offline caching
// src/public/sw.js
const CACHE_NAME = 'dutch-tax-v1'
const urlsToCache = [
  '/',
  '/static/css/main.css',
  '/static/js/main.js',
  '/manifest.json',
]

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => cache.addAll(urlsToCache))
  )
})

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request)
      .then((response) => {
        // Return cached version or fetch from network
        return response || fetch(event.request)
      })
  )
})
```

## Implementation Timeline

### Phase 1: Foundation (Weeks 1-4)
- [x] Project setup and configuration
- [x] Basic component library setup
- [x] Authentication system
- [x] Responsive layout framework

### Phase 2: Core Features (Weeks 5-8)
- [ ] Tax form components
- [ ] Validation framework
- [ ] State management
- [ ] Calculation engine

### Phase 3: Advanced Features (Weeks 9-12)
- [ ] Multi-language support
- [ ] Advanced form features
- [ ] Performance optimization
- [ ] Accessibility enhancements

### Phase 4: Testing & Deployment (Weeks 13-16)
- [ ] Comprehensive testing
- [ ] Security auditing
- [ ] Performance testing
- [ ] Production deployment

## Architecture Benefits

### Scalability
- **Modular Design**: Easy to add new tax forms and features
- **Code Splitting**: Reduces initial bundle size
- **Lazy Loading**: Improves performance for large applications
- **Microservices Ready**: Architecture supports service-oriented design

### Maintainability
- **TypeScript**: Type safety reduces runtime errors
- **Component-Based**: Reusable UI components
- **Clear Separation**: Business logic separated from presentation
- **Comprehensive Testing**: Unit, integration, and E2E testing

### Performance
- **Modern Build Tools**: Vite provides fast development and optimized builds
- **Tree Shaking**: Eliminates unused code
- **Efficient Caching**: Multiple caching strategies
- **Progressive Web App**: Offline capabilities and fast loading

### User Experience
- **Responsive Design**: Works on all devices
- **Accessibility**: WCAG 2.1 compliant
- **Progressive Enhancement**: Works without JavaScript
- **Intuitive Interface**: User-friendly design patterns

## Security Considerations

### Client-Side Security
- **Input Validation**: Comprehensive validation with Zod
- **XSS Protection**: Content Security Policy headers
- **CSRF Protection**: Token-based protection
- **Secure Storage**: Encrypted local storage for sensitive data

### Data Protection
- **Privacy by Design**: Minimal data collection
- **GDPR Compliance**: User consent and data portability
- **Audit Logging**: Comprehensive activity tracking
- **Data Encryption**: End-to-end encryption for sensitive data

## Conclusion

This frontend architecture provides a robust, scalable, and maintainable foundation for the Dutch tax forms web application. The modern technology stack, combined with best practices in responsive design, performance optimization, and security, ensures a high-quality user experience while meeting the complex requirements of tax form processing.

The architecture supports future enhancements and can easily accommodate new tax forms, regulatory changes, and evolving user needs. The comprehensive testing strategy and security measures ensure reliability and compliance with Dutch government standards.

---

**Document Version**: 1.0  
**Last Updated**: July 4, 2025  
**Architecture Team**: Frontend Architecture Planning Agent  
**Review Status**: Ready for Implementation