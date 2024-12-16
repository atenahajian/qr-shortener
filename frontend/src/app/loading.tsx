export default function Loading() {
    return (
      <div className="min-h-screen bg-gray-50 py-12">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <div className="mx-auto max-w-3xl">
            <div className="animate-pulse space-y-8">
              <div className="space-y-4 text-center">
                <div className="mx-auto h-8 w-3/4 rounded bg-gray-200" />
                <div className="mx-auto h-4 w-1/2 rounded bg-gray-200" />
              </div>
              <div className="space-y-4">
                <div className="h-12 rounded-md bg-gray-200" />
                <div className="h-10 rounded-md bg-gray-200" />
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }