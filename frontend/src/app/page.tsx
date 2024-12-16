import { UrlShortenerForm } from '@/components/url-shortener-form';

export default function Home() {
  return (
    <main className="min-h-screen bg-gray-50 py-12">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-3xl">
          <div className="text-center">
            <h1 className="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
              URL Shortener & QR Code Generator
            </h1>
            <p className="mt-4 text-lg text-gray-500">
              Shorten your URLs and generate QR codes instantly
            </p>
          </div>

          <div className="mt-12">
            <UrlShortenerForm />
          </div>
        </div>
      </div>
    </main>
  );
}