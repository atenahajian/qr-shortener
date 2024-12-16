'use client';

import React, { useState } from 'react';
import { useMutation } from '@tanstack/react-query';
import { api } from '@/lib/api';
import { UrlResponse } from '@/lib/types';
import { ArrowPathIcon } from '@heroicons/react/24/outline';

export function UrlShortenerForm() {
  const [url, setUrl] = useState('');

  const { mutate, isPending, data, error } = useMutation({
    mutationFn: async (originalUrl: string) => {
      const response = await api.post<UrlResponse>('/shorten', {
        original_url: originalUrl,
      });
      return response.data;
    },
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (url) {
      mutate(url);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <label htmlFor="url" className="block text-sm font-medium text-gray-700">
          Enter URL to shorten
        </label>
        <div className="mt-1">
          <input
            type="url"
            id="url"
            required
            className="block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            placeholder="https://example.com"
          />
        </div>
      </div>

      <button
        type="submit"
        disabled={isPending}
        className="inline-flex w-full items-center justify-center rounded-md border border-transparent bg-indigo-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 disabled:opacity-50"
      >
        {isPending ? (
          <>
            <ArrowPathIcon className="mr-2 h-4 w-4 animate-spin" />
            Processing...
          </>
        ) : (
          'Shorten URL'
        )}
      </button>

      {error && (
        <div className="rounded-md bg-red-50 p-4">
          <p className="text-sm text-red-700">
            An error occurred. Please try again.
          </p>
        </div>
      )}
    </form>
  );
}
